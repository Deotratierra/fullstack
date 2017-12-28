#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ

# El segundo parámetro es el parámetro por defecto
# si no se encuentra en el hash de las variables de entorno
API_KEY = environ.get("API_KEY", None)

API_KEY = environ["API_KEY"]

print(API_KEY)

''' Fuente:
https://docs.python.org/2/library/os.html
'''
