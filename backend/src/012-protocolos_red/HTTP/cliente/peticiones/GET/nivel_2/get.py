#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#                    Módulo http de la biblioteca estándar

import http.client
import json
from urllib.parse import quote_plus
# La función quote_plus() reemplaza los espacios por signos +
# https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote_plus

base_url = '/maps/api/geocode/json'

def http_GET(address):
    # Especificamos los parámetros de la url
    ruta = '%s?address=%s&sensor=false' % (base_url, quote_plus(address))
    # Realizamos la conexión al servidor
    connection = http.client.HTTPConnection('maps.google.com')
    # Mandamos la petición
    connection.request('GET', ruta)
    # Recogemos la respuesta y la leemos
    rawreply = connection.getresponse().read()
    # Parseamos la respuesta en JSON
    reply = json.loads(rawreply.decode('utf-8'))

    try:
        return reply['results'][0]['geometry']['location']
    except IndexError:
        return reply

# ======================================================================

if __name__ == '__main__':
    print(http_GET('207 N. Defiance St, Archbold, OH'))


""" Fuentes:
Fundamentos de la Programación Web con Python - Brandon Rhodes y John Goerzen
"""
