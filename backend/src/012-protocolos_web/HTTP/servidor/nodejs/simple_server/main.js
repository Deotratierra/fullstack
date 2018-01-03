"use strict"

var http = require('http');

var HOST = "localhost",
    PORT = 8765;

var server = http.createServer(function (req, res) {
  res.write('Hola cliente desde un servidor básico en NodeJS!');
  res.end();
});

server.listen(PORT, HOST, function(){
    console.log("Server running at http://%s:%d", HOST, PORT);
});
