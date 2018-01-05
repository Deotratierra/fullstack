#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# ==========================================

# Objetos de arhivo estándar para manejar
# entradas por consola, salidas y errores
# https://docs.python.org/3/library/sys.html#sys.stdin

# Entradas interactivas (incluidas llamadas a input())
print(sys.stdin)  # <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>

# Salidas de print(), expresiones y avisos de input()
print(sys.stdout) # <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>

# Avisos del intérprete y mensajes de error:
print(sys.stderr) # <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>


# Esos canales (streams) son archivos de texto regulares
# tales como aquellos devueltos por la función open()


# ==========================================

# La manera más fácil de crear un canal
# de texto es con la función open().
# Realmente es la función io.open() de la biblioteca io
f = open("../archivo.txt", "r", encoding="UTF-8")
print(f) # <_io.TextIOWrapper name='../archivo.txt' mode='r' encoding='UTF-8'>


import io

# También están disponibles los canales
# en memoria con la biblioteca io
f = io.StringIO("Un poco de texto por aquí")
print(f)  # <_io.StringIO object at 0x7f5237eb5948>

"""
Hay tres tipos principales de canales en io,
de los cuales heredan otros tipos:
- Entrada/salida de texto
- Entrada/salida en binario
- Entrada/salida cruda
"""

# Podemos crear canales de datos en binario
with open("../imagen.png", "rb") as f:
    print(f)  # <_io.BufferedReader name='../imagen.png'>

f = io.BytesIO(b"Datos en binario: \x00\x01")
print(f)  # <_io.BytesIO object at 0x7ff201bf6f10>

###   Métodos de los canales   ###

# Comprobar si el canal es interactivo (si está
# conectado a una terminal o a un dispositivo tty)
print(f.isatty())  # False

# Comprobar si es un canal leíble
print(f.readable()) # True

# Obtener las líneas en una lista
print(f.readlines()) # [b'Datos en binario: \x00\x01']

# Comprobar si el canal es escribible
print(f.writable()) # True

# No te olvides de cerrar los canales
print(f.closed) # False
f.close()
print(f.closed) # True

# ==========================================

# Fuentes:
# https://docs.python.org/3/library/io.html
# https://askubuntu.com/questions/481906/what-does-tty-stand-for