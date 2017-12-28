"use strict"

// npm install -g mocha
var chai = require("chai"); // npm install chai

var youtube = require("../youtube"); 

// Sobreescribimos las aserciones por defecto
// por las de la biblioteca chai
var assert = chai.assert;  

// ################  CONFIGURACIÓN DE LOS TESTS  ################

class Config {
    constructor() {
        this.YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;
        this.MY_CHANNEL_ID = "UCAgyf7c-giXPM0zgEExB74w";
        this.VIDEO_URL = "https://www.youtube.com/watch?v=zAPEHIzHPT4";
    }
}

var config = new Config();
var client = new youtube.YoutubeApi(config.YOUTUBE_API_KEY);


// ################  TESTTING CON MOCHA Y CHAI  ################
// http://chaijs.com/api/assert/
// https://github.com/ideaq/learn-mocha


describe("YoutubeApi tests\n", function(){

    describe("client.channel_videos()", function(){
        it("Retorna un array con la info de los vídeos del canal", function(){
            assert.isArray(client.channel_videos(config.MY_CHANNEL_ID));
        })
    });

    describe("client.search_channel()", function(){
        it("Retorna un objeto con la información del canal", function(){
            assert.isObject(client.search_channel(config.MY_CHANNEL_ID));
        })
    });

    describe("client.search_video()", function(){
        it("Retorna un objeto con la información del video", function(){
            assert.isObject(client.search_video(config.VIDEO_URL));
        })
    });

    describe("client.channel_video_urls()", function(){
        it("Retorna un array las urls de los vídeos del canal", function(){
            assert.isArray(client.channel_video_urls(config.MY_CHANNEL_ID));
        })
    });

    describe("client.search_by_tag()", function(){
        it("Retorna un array con vídeos relacionados a la búsqueda", function(){
            assert.isArray(client.search_by_tag("Medicina germánica"));
        })
    });

    describe("client.video_comments()", function(){
        it("Retorna un objeto con los comentarios de un vídeo", function(){
            assert.isObject(client.video_comments(config.VIDEO_URL));
        })
    });

});


/* 
Para lanzar los tests (deben estar en un directorio llamado test), ejecutar:
mocha
*/ 