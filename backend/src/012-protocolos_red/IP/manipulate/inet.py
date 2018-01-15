#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

IPv4 = "192.168.1.12"
IPv6 = "2001:db8:a0b:12f0::1"

""" Cuando estamos trabajando con funciones de red de bajo nivel, a veces,
la notación usual de cadenas de las direcciones IP no es muy util.
Hay que convertirlas a paquetes binarios de 32 bit """

from binascii import hexlify # Representación hexadecimal de datos en binario
# https://docs.python.org/3/library/binascii.html#binascii.hexlify

def pack_ipv4_address(address):
    # Empaquetar IPv4 a paquete binario de 32 bits
    packed_ip_addr = socket.inet_aton(address)
    # Desempaquetar IPv4 desde paquete binario de 32 bits
    unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
    print("Dirección IP: %s  |  Empaquetada: %s  (Objeto %r)" % \
            (unpacked_ip_addr, hexlify(packed_ip_addr), packed_ip_addr))

def pack_ipv6_address(address):
    # Empaquetar IPv6 a paquete binario de 32 bits
    packed_ip_addr = socket.inet_pton(socket.AF_INET6, address) # Para IPv4 usar AF_INET
    # Desempaquetar IPv6 desde paquete binario de 32 bits
    unpacked_ip_addr = socket.inet_ntop(socket.AF_INET6, packed_ip_addr)
    print("Dirección IP: %s  |  Empaquetada: %s  (Objeto %r)" % \
            (unpacked_ip_addr, hexlify(packed_ip_addr), packed_ip_addr))

""" Estas funciones son útiles conversando con un programa que use la biblioteca
estándar de C y necesite objetos de tipo in_addr, el cual es el tipo de C
de 32 bits binarios que retorna la función. Para más información ejecutar: man inet
Levanta socket.error si la dirección no es válida."""


if __name__ == "__main__":
    pack_ipv4_address(IPv4)
    # Para saber si tu plataforma soporta ipv6
    if socket.has_ipv6:
        pack_ipv6_address(IPv6)
    else:
        print("Tu plataforma no soporta IPv6")