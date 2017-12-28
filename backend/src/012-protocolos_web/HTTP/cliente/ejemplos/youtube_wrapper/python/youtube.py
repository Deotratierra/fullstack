#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlencode
from json import loads
from re import findall

YOUTUBE_COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_VIDEO_OEMBED = "https://www.youtube.com/oembed"
YOUTUBE_VIDEO_RESULTS = "https://www.youtube.com/results"

class YoutubeApi(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def _openURL(self, url, parms):
        """Función interna para construir la URL
        y construir la petición"""
        f = urlopen("%s?%s" % (url, urlencode(parms)))
        data = f.read()
        f.close()
        return data.decode("utf-8")

    def channel_videos(self, channel_id, max_res=50):
        """Toma una id de canal y devuelve todos los vídeos
        con su información en un diccionario. Se le puede pasar
        un número para indicar el límite máximo de resultados"""
        parms = {
                   "part": "id,snippet",
                   "channelId": channel_id,
                   "maxResults": max_res,
                   "key": self.api_key
                }

        matches = self._openURL(YOUTUBE_SEARCH_URL, parms)
        search_response = loads(matches)

        videos = []
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append(search_result["snippet"])
        return videos

    def search_channel(self, channel_id, max_res=50):
        """Toma una id de canal y devuelve información sobre el canal"""
        parms = {
                    "part": "snippet",
                    "channelId": channel_id,
                    "key": self.api_key,
                    "maxResults": max_res,
                }

        return loads(self._openURL(YOUTUBE_SEARCH_URL, parms))

    def search_video(self, url):
        """Toma la url de un vídeo y devuelve su información"""
        parms = {
                    "url": url,
                    "json": "json"                     
                }
        return loads(self._openURL(YOUTUBE_VIDEO_OEMBED, parms))

    def channel_video_urls(self, channel_id, max_res=50):
        """Toma el ID de un canal y devuelve las urls de los vídeos"""
        videos = self.search_channel(channel_id, max_res=max_res)["items"]
        base_url = "https://www.youtube.com/watch?v="
        response = []
        for video in videos:
            if len(response) >= max_res: break
            if video["id"]["kind"] == "youtube#video":
                videoId = video["id"]["videoId"]
                response.append(base_url + videoId)
        return response

    def search_by_tag(self, tags, max_res=50):
        """Devuelve una lista de urls de vídeos relacionados
        a los tags pasados como argumento"""
        parms = {"search_query": tags}
        html = self._openURL(YOUTUBE_VIDEO_RESULTS, parms)
        search_results = findall(r"href=\"\/watch\?v=(.{11})", html)
        response = []
        for id in search_results:
            if len(response) >= max_res: break
            response.append("http://www.youtube.com/watch?v=" + id)
        return response

    def video_comments(self, video_url, max_res=50):
        """Retorna los comentarios del video pasado como url"""
        video_id = video_url.split("watch?v=")[1]
        parms = {
                   "part": "id,snippet",
                   "videoId": video_id,
                   "maxResults": max_res,
                   "key": self.api_key
                }
        matches = self._openURL(YOUTUBE_COMMENT_URL, parms)
        return loads(matches)["items"]

