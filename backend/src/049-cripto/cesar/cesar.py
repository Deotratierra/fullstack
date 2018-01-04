#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getch import getch  # pip3 install getch

def cifrar(texto, clave):
    response = ""
    for ch in texto:
        response += chr(ord(ch) + clave)
    return response

def descifrar(texto, clave):
    response = ""
    for ch in texto:
        response += chr(ord(ch) - clave)
    return response

if __name__ == "__main__":
    clave, accion, texto = None, None, None

    while not clave:
        print("Selecciona una clave de cifrado: ")
        try:
            clave = int(getch())
        except ValueError as e:
            print("La clave debe ser un número entero")

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
