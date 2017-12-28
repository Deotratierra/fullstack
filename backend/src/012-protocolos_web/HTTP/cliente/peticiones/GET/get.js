'use strict'

var URL = "https://min-api.cryptocompare.com/stats"


// ==================================================

// ------ ASÍNCRONA ---------------------------------  request
// npm install request
// https://github.com/request/request

var request = require("request");


var request_GET = function(url){
    request(url, function (error, response, body) {
        if (error) {
            throw error;
        } else {
            if (response.statusCode == 200){
                //console.log(JSON.parse(body));  //  <--- En JSON
                console.log(body);
            } else {
                console.error("Error en la petición GET síncrona con request.");
                console.error("Status code == " + response.statusCode);
            };
        };
    });
};

// ==================================================

// ------ ASÍNCRONA ---------------------------------  urllib
// npm install urllib --save
// https://www.npmjs.com/package/urllib

var urllib = require("urllib");

var urllib_GET = function(url){
    urllib.request(url, function(error, data, response){
        if (error){
            throw error;
        } else {

        } if (response.statusCode == 200){
            //console.log(JSON.parse(data.toString()));  //  <--- En JSON
            console.log(data.toString());
        } else {
            console.error("Error en la petición GET síncrona con urllib.");
            console.error("Status code == " + response.statusCode);
        };
    });
};

// ==================================================


if (require.main === module) {
  request_GET(URL);
  urllib_GET(URL);
};
