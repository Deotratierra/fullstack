#!/usr/bin/ruby

require "socket" # Provee las clases TCPServer y TCPSocket

HOST = "localhost"
PORT = 8765

server = TCPServer.new(HOST, PORT)

puts "Server running at http://#{HOST}:#{PORT}"

# Loop infinito que procesa sólo una conexión entrante a la vez.
loop do

    # Espera a que el cliente se conecte, entonces
    # devuelve un objeto TCPSocket que puede ser usado
    # de forma similar a otros objetos I/O de Ruby.
    # (De hecho, TCPSocket es una subclase de IO)
    socket = server.accept

    # Lee la primera línea de la petición
    request = socket.gets

    # Loguea la petición en la consola para depuración
    STDERR.puts request           # GET / HTTP/1.1

    response = "Hola cliente desde un servidor minimalista de Ruby!\n"

    # Necesitamos incluir las cabeceras Content-Type y Content-Length
    # para permitir al cliente conocer el tamaño y el tipo de
    # la información contenida en la respuesta.

    socket.print "HTTP/1.1 200 OK\r\n" +
                 "Content-Type: text/plain\r\n" +
                 "Content-Length: #{response.bytesize}\r\n" +
                 "Connection: close\r\n"

    # Imprime una línea en blanco para separar el cabecero del
    # cuerpo de la respuesta como requiere el protocolo.
    socket.print "\r\n"

    # Imprime el cuerpo actual de la respuesta
    socket.print response

    # Cierra el socket y termina la conexión
    socket.close
end
