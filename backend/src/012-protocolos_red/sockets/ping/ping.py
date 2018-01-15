#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform
import socket

def multiplatform_ping(address):
    """Realiza un PING multiplataforma. Devuelve True si
    el servidor devuelve datos, False en caso contrario."""
    oper = platform.system()
    if (oper=="Windows"):
        command = "ping -n 1 "
    elif (oper== "Linux"):
        command = "ping -c 1 "
    else :
        command = "ping -c 1 "
    response = os.popen(command + address)

    on = False
    for line in response.readlines():
        if line.count("ttl") or line.count("TTL"):
            on = True
            break
    return on


if __name__ == "__main__":
    print(multiplatform_ping(socket.gethostbyname("www.github.com")))
