#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
El módulo pickle de Python traduce cualquier objeto en memoria
en una cadena de bytes serializada que puede ser escrita en cualquier
objeto de tipo archivo
"""

import os
import pickle

def guardar(datos, archivo):
    """Serializar datos"""
    with open(archivo, 'ab') as dbfile:  # Es importante usar el modo binario
        pickle.dump(datos, dbfile)                # Los parámetros son fuente y destino

def cargar(archivo):
    """Deserializar datos"""
    with open(archivo, "rb") as dbfile:
        response = pickle.load(dbfile)
    return response


if __name__ == "__main__":
    datos = {"clave1": True, "clave2": False}
    archivo = "ejemplo"

    """Guardamos el diccionario en un archivo"""
    guardar(datos, archivo)
    """Obtenemos el diccionario del archivo"""
    respuesta = cargar(archivo)
    print(respuesta, type(respuesta))  # {'clave1': True, 'clave2': False} <class 'dict'>

    os.remove(archivo)
