#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Obtener tiempo de expiración
    print("Tiempor de expiración del socket por defecto: %s" % sock.gettimeout())

    # Establecer tiempo de expiración
    sock.settimeout(100)

    print("Tiempo de expiración del socket actual: %s" % sock.gettimeout())

# ==================================================================

""" Fuentes:
Libro de cocina de Programación Web con Python - Dr. M. O. Faruque sarker
"""
