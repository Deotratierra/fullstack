#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Abrir archivos en modo escritura
with open("ejemplo.txt", "w") as archivo:
    # Escribir en archivos
    archivo.write("Contenido del archivo\n")

# Abrir archivos en modo lectura
with open("ejemplo.txt", "r") as archivo:
    # Leer archivos
    contenido = archivo.read()
    # Obtener contenido en lista
    lineas = archivo.readlines()
