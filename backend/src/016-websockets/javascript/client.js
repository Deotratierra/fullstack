var WebSocket = require("ws");  // npm install ws

var HOST = "localhost",
    PORT = 8765;

var client = function(host, port){

    var ws = new WebSocket("ws://" + host + ":" + port);

    ws.on("open", function open() {
      ws.send('PING');
    });

    ws.on("message", function incoming(data) {
      console.log(data);
    });

    ws.on("error", function error(error){
        console.error(error);
    })
}

if (require.main == module){
    client(HOST, PORT);
}

/* Fuente:
https://github.com/websockets/ws
*/