#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# Por defecto, los sockets en Python se
# crean de la familia AF_INET, de tipo SOCK_STREAM
sock = socket.socket()

# Enlazamos el socket con un servidor y un puerto:
sock.bind(("localhost", 8765))

# Ponemos en escucha al socket, indicando el número
# de conexiones máximas simultáneas permitidas.
# Si no definimos este número se define por defecto
# un valor razonable
sock.listen(10)

# Comenzamos a aceptar conexiones. El método accept
# recibe la conexión del cliente, así como su dirección.
try:
    client_conn, (client_host, client_port) = sock.accept()
except KeyboardInterrupt:
    print("\nSocket cerrado antes de recibir clientes.")
    exit(0)

# Para recibir una conexión utilizamos el método recv()
# que toma como parámetro los bytes máximos a aceptar:
while True:
    recibido = client_conn.recv(1024)
    print("> Recibido:", recibido)

    # Para enviar datos de vuelta al cliente usamos
    # el método send():
    print("< Enviando:", recibido)
    client_conn.send(recibido)

    if recibido in (b"close", b"quit"):
        break


# Para cerrar una conexión usamos el método close()
sock.close()
print("Conexión cerrada")


# Fuentes:
# https://docs.python.org/3/library/socket.html
