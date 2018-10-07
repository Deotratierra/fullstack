#!/usr/bin/ruby

require "websocket-client-simple"  # gem install websocket-client-simple

HOST, PORT = "localhost", 8765

def client(host, port)
    ws = WebSocket::Client::Simple.connect "ws://%s:%d" % [host, port]

    ws.on :message do |msg|
        puts "#{msg.data}"
    end

    ws.on :open do
        ws.send "PING"
    end

    ws.on :close do |e|
        p e
        exit 1
    end

    ws.on :error do |e|
        p e
    end

    loop do
        ws.send STDIN.gets.strip
    end
end

if __FILE__ == $0
    client(HOST, PORT)
end

=begin
Fuente:
https://github.com/shokai/websocket-client-simple
=end
