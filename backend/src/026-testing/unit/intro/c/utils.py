#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cffi   # pip3 install cffi
import importlib


def load(filename):
    """Función que toma un nombre de archivo sin su extensión
    ubicado en el mismo directorio y carga dos archivos con dicho
    nombre con las extensiones .c y .h

    Args:
        filename (str): Ruta al archivo/s sin extensión.

    Returns:
        Modulo que puentea el código C y lo hace
        disponible desde Python.
    """
    # Cargamos el código fuente
    with open("%s.c" % filename, "r") as f:
        source = f.read()
    with open("%s.h" % filename, "r") as f:
        includes = f.read()



    # Pasamos el código fuente a CFFI
    ffibuilder = cffi.FFI()
    ffibuilder.cdef(includes)
    ffibuilder.set_source("%s_" % filename, source)
    ffibuilder.compile()

    # Importa y devuelve el módulo resultante
    module = importlib.import_module("%s_" % filename)
    return module.lib

def clean(filename):
    """Borra el archivo C generado por cffi
    pasando como argumento el nombre introducido
    en la función load() al generarlo y todos los
    archivos con extensión .so

    Args:
        filename (str): Ruta al archivo/s sin extensión.
    """
    os.remove("%s_.c" % filename)
    dir_name = os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(dir_name):
        if f.endswith(".so"):
            os.remove(os.path.join(dir_name, f))


