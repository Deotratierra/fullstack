#!/usr/bin/ruby

require 'em-websocket' # gem install em-websocket

HOST, PORT = "localhost", 8765

def server(host, port)
    EM.run {
        EM::WebSocket.run(:host => host, :port => port) do |ws|
            ws.onopen { |handshake|
                puts "WebSocket connection open"

            # Acceso a las propiedades en el objeto EM::WebSocket::Handshake,
            # por ejemplo: path, query_string, origin, headers
            }

            ws.onclose { puts "Connection closed" }

            ws.onmessage { |msg|
                puts "< #{msg}"

                if msg == "PING"
                    puts "> PONG"
                    ws.send "PONG"
                end               
                
            }
        end
    }
end

if __FILE__ == $0
    server(HOST, PORT)
end

=begin
Fuente:
https://github.com/igrigorik/em-websocket
=end
