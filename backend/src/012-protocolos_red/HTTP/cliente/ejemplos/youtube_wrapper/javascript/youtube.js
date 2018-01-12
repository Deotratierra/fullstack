"use strict"

// npm install sync-request
var request = require("sync-request"); // Llamadas síncronas


var YOUTUBE_COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads",
    YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search",
    YOUTUBE_VIDEO_OEMBED = "https://www.youtube.com/oembed",
    YOUTUBE_VIDEO_RESULTS = "https://www.youtube.com/results"

class YoutubeApi {
    constructor(api_key){ this.api_key = api_key; }

    /* Función interna para convertir diccionarios
       en parámetros de una URL 

       @param obj Diccionario a serializar

       @return Parametros serializados para la URL */
    _serialize(obj){
        var str = [];
        for (var p in obj){
            str.push(p + "=" + obj[p]);
        }
        return str.join("&");
    }

    /* Función interna para obtener la respuesta 
       de una llamada.

       @param url URL base de youtube de la llamada
       @param parms Diccionario de parámetros
       @param json Si es true, devuelve la respuesta en JSON
           (opcional, por defecto == true)

       @return Respuesta de la llamada */
    _openURL(url, parms, json=true){
        url += "?" + this._serialize(parms);
        var response = request("GET", url);
        if (json){
            return JSON.parse(response.getBody("utf-8"))
        }
        return response.getBody("utf-8")
    };

    // Devuelve la información de los vídeos de 
    // un canal pasando su id como argumento
    channel_videos(channel_id, max_res=50){
        var parms = {
                        part: "id,snippet",
                        channelId: channel_id,
                        maxResults: max_res,
                        key: this.api_key
                    }
        var matches = this._openURL(YOUTUBE_SEARCH_URL, parms),
            videos = [];
        matches = matches.items;
        if (matches.length > 0){
            for (var i = 0; i < matches.length; i++) {
                if (matches[i].id.kind == "youtube#video"){
                    videos.push(matches[i].snippet)
                }
            };
        };
        return videos
    };

    // Toma la id de un canal y devuelve su información
    search_channel(channel_id){
        var parms = {
                        part: "snippet",
                        channelId: channel_id,
                        key: this.api_key
                    }
        return this._openURL(YOUTUBE_SEARCH_URL, parms);
    };

    // Toma la url de un vídeo y devuelve su información
    search_video(url){
        var parms = {
                        url: url,
                        json: "json"                     
                    }
        return this._openURL(YOUTUBE_VIDEO_OEMBED, parms);
    };

    // Toma el ID de un canal y devuelve las urls de los vídeos
    channel_video_urls(channel_id, max_res=50){
        var videos = this.search_channel(channel_id, max_res=max_res).items,
            base_url = "https://www.youtube.com/watch?v=", response = [];
        for (var i = 0; i < videos.length; i++) {
            if (response.length >= max_res){ break; }
            if (videos[i].id.kind == "youtube#video"){
                var videoId = videos[i].id.videoId;
                response.push(base_url + videoId);
            }
        };
        return response
    };

    // Devuelve una lista de urls de vídeos relacionados
    // a los tags pasados como argumento
    search_by_tag(tags, max_res=50){
        var parms = {search_query: tags}, response = [];
        var html = this._openURL(YOUTUBE_VIDEO_RESULTS, parms, false);
        var re = /href=\"\/watch\?v=(.{11})/g;
        var search_results = html.match(re);
        for (var i = 0; i < search_results.length; i++) {
            if (response.length >= max_res){ break; }
            response.push("http://www.youtube.com/watch?v=" + search_results[i])
        };
        return response    
    };

    // Retorna los comentarios del video pasado como url
    video_comments(video_url, max_res=50){
        var video_id = video_url.split("watch?v=")[1]
        var parms = {
                        part: "id,snippet",
                        videoId: video_id,
                        maxResults: max_res,
                        key: this.api_key
                    }
        return this._openURL(YOUTUBE_COMMENT_URL, parms)
    };
};


module.exports = {
    YoutubeApi: YoutubeApi
}


/* Fuentes:
https://stackoverflow.com/questions/6323417/how-do-i-retrieve-all-matches-for-a-regular-expression-in-javascript
*/