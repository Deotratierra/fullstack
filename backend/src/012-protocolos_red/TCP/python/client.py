#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from time import sleep

sock = socket.socket()

# Para conectarnos a un socket
# utilizamos el método connect():
sock.connect(("localhost", 8765))

messages = ["Hola", "close"]

for msg in messages:
    # La codificación en bytes es necesaria:
    print("< Enviando:", msg.encode())
    sock.send(msg)

    # Decodificamos al recibir
    recibido = sock.recv(1024).decode()
    print("> Recibido:", recibido)

    if recibido in ("quit", "close"):
        break

    sleep(3)

print("Conexión cerrada")
