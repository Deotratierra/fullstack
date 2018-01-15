#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

PUERTOS = range(0, 65536)  # 65535 puertos
PROTOCOLOS = ["tcp", "udp"]
IP = socket.gethostbyname("www.github.com")  # Para tu IP, arg: socket.gethostname()

def find_services(address):
    for puerto in PUERTOS:
        for protocolo in PROTOCOLOS:
            try:
                print("Puerto: %5d  =>  Servicio: %20s  |   Protocolo: %s" % \
                     (puerto, socket.getservbyport(puerto, protocolo), protocolo)
                )
                break
            except OSError:  # No se encuentra servicio
                pass
                #print("Protocolo %s no encontrado en el puerto %d" % (protocolo, puerto))

if __name__ == '__main__':
    find_services(IP)