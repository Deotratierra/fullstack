#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from time import sleep

# Por defecto (sin argumentos), los sockets se abren en modo TCP e IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

    if recibido in ("quit", "close", "off"):
        break

    sleep(3)

print("Conexión cerrada")
