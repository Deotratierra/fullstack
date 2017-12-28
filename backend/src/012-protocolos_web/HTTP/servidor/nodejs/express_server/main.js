"use strict"

var express 	= require('express');  // npm install express
var app 		= express();

var HOST = "localhost",
    PORT = 8080;

// Handlers
app.get('/', function (req, res) {
  res.send('¡Hola mundo en Express!');
});


// Escucha en el puerto 8080 y corre el server
app.listen(PORT, HOST, function() {
	console.log("App listening at " + HOST + ":" + PORT);
});
