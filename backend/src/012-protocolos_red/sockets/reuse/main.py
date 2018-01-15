#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Si corres un socket e Python en un puerto específico e intentas volver a correrlo
antes de cerrarlo, no serás capaz de usarlo. Normalmente te saldrá el error:

-----------------------------------------------------------------------
Traceback (most recent call last):
    File "1_10_reuse_socket_address.py", line 40, in <module>
        reuse_socket_addr()
    File "1_10_reuse_socket_address.py", line 25, in reuse_socket_addr
        srv.bind( ('', local_port) )
    File "<string>", line 1, in bind
socket.error: [Errno 98] Address already in use
-----------------------------------------------------------------------

El remedio a este problema es a este problema es activar la opción de reutilización
de direcciones en un socket: SO_REUSEADDR
"""

import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def show_reuse_opt():
        # Obtener si estamos usando la opción de reutilización de direcciones
        response = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print("¿Estamos reutilizando la reutilización de direcciones? %s" % \
                ("SI" if response == 1 else "NO") )
        return response

    reutilizando = show_reuse_opt()

    if reutilizando == 0:
        # Establecer la reutilización de direcciones
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        show_reuse_opt()
