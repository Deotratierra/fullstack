#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Por defecto, los bloques operan en modo bloqueante. Por ejemplo, si llamas
a la función connect(), la conexión bloqueará tu programa hasta que la operación
haya sido completada. En muchas ocasiones, no quieres que tu programa espere
para siempre hasta una respuesta del servidor o un error que detenga tu operación.
Para ello lo pones en modo asíncrono y puedes ejecutar otras tareas mientras."""

import socket

ADDRESS = "127.0.0.1"
PORT = 8765   # 0 indica al núcleo que seleccione un puerto libre de forma automática

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establecer el socket en modo bloqueante
    sock.setblocking(1)  # Configuración por defecto

    # Establecer el socket en modo no bloquante
    sock.setblocking(0)
    # https://docs.python.org/3/library/socket.html#socket.socket.setblocking

    sock.settimeout(.5)   # Ver tiempos de expiración
    sock.bind((ADDRESS, PORT))

    socket_address = sock.getsockname()

    print("Socket lanzado en %s" % str(socket_address))
    while True:
        sock.listen(1)

# =============================================================

""" Fuentes:
Libro de cocina de Programación Web con Python - Dr. M. O. Faruque sarker
"""
