
var WebSocket = require("ws");  // npm install ws

var HOST = "localhost",
    PORT = 8765;

var server = function(host, port){
    var wss = new WebSocket.Server({ host: host, port: port });

    wss.on("connection", function connection(ws) {
        ws.on("message", function incoming(message) {
            console.log("< %s", message);
            if (message == "PING"){
                console.log("> PONG")
                ws.send("PONG");
            }
        });
    });

};

if (require.main == module){
    server(HOST, PORT);
}

/* Fuente:
https://github.com/websockets/ws
*/