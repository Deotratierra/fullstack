#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Con os métodos getsockopt() y setsockopt() de un socket podemos obtener y modificar
las propiedades de un objeto socket respectivamente. El método setsockopt() toma 3 argumentos:
el nivel al que va a afectar la opción establecidam, el nombre de la opción y el nuevo valor.
Para más información sobre ambas funciones ejecutar: man getsockopt
"""


import socket

ENTRADA = 4096
SALIDA = 4096

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def show_sizes():
        # Obtener el tamaño de buffer
        bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        print("Tamaño de entrada del buffer: %d" % bufsize)
        print("Tamaño de salida del buffer: %d" % bufsize)

    show_sizes()

    # Establecer el tamaño de buffer
    #sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SALIDA)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, ENTRADA)

    show_sizes()

# ==================================================================

""" Fuentes:
Libro de cocina de Programación Web con Python - Dr. M. O. Faruque sarker
"""



