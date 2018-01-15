#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import argparse
import logging

"""Este script toma un host (IPV4, IPv6 o HTTP) e imprime todos
    los servicios corriendo los puertos seleccionados (por defecto todos)."""

PROTOCOLOS = ["tcp", "udp"]

# Logging
__format__ = "%(asctime)s - %(name)s - %(levelname)s  -->  %(message)s"
logging.basicConfig(format=__format__)
logger = logging.getLogger(__file__.split(".")[0])

# ==================================================================================
#                           Find services by port

def find_services(address, ports):
    for puerto in ports:
        for protocolo in PROTOCOLOS:
            try:
                print("Puerto: %5d  =>  Servicio: %20s  |   Protocolo: %s" % \
                     (puerto, socket.getservbyport(puerto, protocolo), protocolo)
                )
                break
            except OSError:  # No se encuentra servicio
                pass
                #print("Protocolo %s no encontrado en el puerto %d" % (protocolo, puerto))

# ==========================================================================================

def parse_args():
	"""Script arguments parsing"""
    desc = "Escanea todos los servicios activos en una dirección de internet pasada como" + \
        " HTTP o IP e imprime los resultados. Se puede determinar un rango de puertos."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("address", help="Dirección a escanear. Puede ser HTTP, IPv4 o IPv6.",
                         type=str)
    parser.add_argument("--ports", "-p", help="Rango de puertos donde buscar los servicios.",
    	                nargs="+", type=int)
    parser.add_argument("--debug", "-d", dest="debug",
    	                help="Mostrar mensajes de DEBUG.", action="store_true")

    return parser.parse_args()

# -------------------------------------------------------------------------------

def clean_address(addr):
	"""Comprueba si la dirección pasada es IPv4, IPv6 o HTTP,
	para otorgar mayor flexibilidad al usar el script"""
    try:   # ¿Es una dirección IPv4?
        socket.inet_aton(addr)
        logger.debug("IPv4 address found: %s", addr)
        return addr
    except socket.error:
        try: # ¿Es una dirección IPv6?
            socket.inet_pton(socket.AF_INET6, addr)
            logger.debug("IPv6 address found: %s", addr)
            return addr
        except socket.error: # Es una dirección HTTP
            logger.debug("HTTP address found: %s", addr)
            return socket.gethostbyname(addr)

# ==========================================================================================

if __name__ == '__main__':
    args = parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    # Dirección y puertos a buscar
    address = clean_address(args.address)
    if not args.ports:
        ports = range(0, 65536)
    else:
        ports = range(args.ports[0], args.ports[1]+1)

    find_services(address, ports)
