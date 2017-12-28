#!/usr/bin/ruby

require "uri" # <-- Convertir un hash en los parámetros de una url
require "httparty" # gem install httparty

YOUTUBE_COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_VIDEO_OEMBED = "https://www.youtube.com/oembed"
YOUTUBE_VIDEO_RESULTS = "https://www.youtube.com/results"

class YoutubeApi
    def initialize(api_key)
        @api_key = api_key
    end

    # Función interna para construir la URL de las llamadas
    def _openURL(url, parms, json=true)
        url += "?" + URI.encode_www_form(parms)
        response = HTTParty.get(url)
        if json
            response.parsed_response # <-- En JSON
        else
            response
        end
    end
    
    # Toma la id de un canal y devuelve todos sus
    # vídeos con su información
    def channel_videos(channel_id, max_res=50)
        parms = {
                   "part" => "id,snippet",
                   "channelId" => channel_id,
                   "maxResults" => max_res,
                   "key" => @api_key
                }
        matches = self._openURL(YOUTUBE_SEARCH_URL, parms)
        videos = []
        for search_result in matches.fetch("items", [])
            if (search_result["id"]["kind"] == "youtube#video")
                videos.push(search_result["snippet"])
            end
        end
        videos
    end

    # Toma la id de un canal y devuelve su información
    def search_channel(channel_id, max_res=50)
        parms = {
                   "part" => "id,snippet",
                   "channelId" => channel_id,
                   "key" => @api_key,
                   "maxResults" => max_res
                }
        return self._openURL(YOUTUBE_SEARCH_URL, parms)
    end

    # Toma la url de un vídeo y devuelve su información
    def search_video(url)
        parms = {
                    "url" => url,
                    "format" => "json"
                }
        return self._openURL(YOUTUBE_VIDEO_OEMBED, parms)
    end

    # Toma la ID de un canal y devuelve las URLs de sus vídeos
    def channel_video_urls(channel_id, max_res=50)
        videos = self.search_channel(channel_id, max_res=max_res)["items"]
        base_url = "https://www.youtube.com/watch?v="
        response = []
        for video in videos
            if (response.length >= max_res); break; end;
            if (video["id"]["kind"] == "youtube#video")
                videoId = video["id"]["videoId"]
                response.push(base_url + videoId)
            end
        end
        return response
    end

    # Devuelve una lista de vídeos relacionados
    # a los tags pasados como argumento 
    def search_by_tag(tags, max_res=50)
        parms, response = {"search_query" => tags}, []
        html = self._openURL(YOUTUBE_VIDEO_RESULTS, parms, json=false)
        search_results = html.scan(/href=\"\/watch\?v=(.{11})/) 
        for id in search_results  #  id.class == Array
            if (response.length >= max_res); break; end;
            response.push("http://www.youtube.com/watch?v=" + id[0])
        end
        return response
    end

    # Retorna los comentarios del video pasado como url
    def video_comments(video_url, max_res=50)
        video_id = video_url.split("watch?v=")[1] # Igual en Python
        parms = {
                   "part" => "id,snippet",
                   "videoId" => video_id,
                   "maxResults" => max_res,
                   "key" => @api_key
                }
        return self._openURL(YOUTUBE_COMMENT_URL, parms)
    end
end

=begin
Fuentes:
https://stackoverflow.com/questions/39549244/how-to-get-a-default-value-with-hashes-in-ruby
https://stackoverflow.com/questions/80357/match-all-occurrences-of-a-regex
=end
