#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import ceil
from getch import getch  # pip3 install getch

def cifrar(texto, n):
    ancho = ceil(len(texto) / n)
    return ''.join([texto[linea::n].ljust(ancho) for linea in range(n)]).rstrip()

def descifrar(texto_cifrado, n):
    return cifrar(texto_cifrado, ceil(len(texto_cifrado) / n))

if __name__ == "__main__":
    clave, accion, texto = None, None, None

    while not clave:
        print("Selecciona una clave de cifrado: ")
        try:
            clave = int(getch())
        except ValueError:
            print("Introduce un número entero")

    while not accion:
        print("Selecciona una acción:\n\t1. Cifrar\n\t2. Descifrar")
        map_sel = {"1": "cifrar", "2": "descifrar"}
        try:
            accion = map_sel[getch()]
        except KeyError:
            print("Acción no disponible\n")

    while not texto:
        texto = input("Inserta un texto a %s: " % accion)
    print("\nResultado:", eval("%s(texto, clave)" % accion))


# Fuente:
# http://www.solveet.com/exercises/Criptografia-La-Escitala-Espartana/147/solution-992
