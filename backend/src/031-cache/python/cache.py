#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cachetools  # pip3 install cachetools
# http://cachetools.readthedocs.io/en/latest/

# Cache simple:
# https://github.com/tkem/cachetools/blob/master/cachetools/cache.py
cachetools.Cache()

# Se accede a ellas e insertan como un diccionario

# Time to live (cache que expira con el tiempo)
ttl = cachetoolsTTLCache(128, 60)
# El primer parámetro es el tamaño de la cache,
# el número de elementos que puede guardar.
# El segundo parámetro es la cantidad de segundos que
# duran los elementos almacenados en la caché

# ----------------------------------------------------

# También existe una implementación en la biblioteca con
# decoradores para funciones

from cachetools.func import *

@ttl_cache(128, 60)
