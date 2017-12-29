#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

ARCHIVO = "../README.md"

# Obtener el tamaño en bytes de un archivo
print(os.path.getsize(ARCHIVO))

# Obtener la fecha del último acceso (en Unix timestamps)
print(os.path.getatime(ARCHIVO))

# Obtener la fecha de la última modificación (en Unix timestamps)
print(os.path.getmtime(ARCHIVO))

# Obtener fecha del último cambio dentro del archivo (en Unix timestamps)
print(os.path.getctime(ARCHIVO))

# Obtener todos los atributos de metadatos de un archivo
print(os.stat(ARCHIVO))
# Lista de atributos:
# https://docs.python.org/3/library/os.html#os.stat_result
