#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compat_bytes(item, encoding=None):
    """Esta función es necesaria debido a que la función ``bytes()``
    de Python2.7 es simplemente un alias para ``str()``.

    :param item: Objeto cuyo método ``__bytes__`` necesita ser invocado.
    :param encoding: Parámetro de codificación opcional para menjar
        el segundo argumento de la función ``bytes()`` de Python3.6

    :return: Un objeto bytes que funciona igual en Python 3.6 y 2.7
    """
    if hasattr(item, '__bytes__'):
        return item.__bytes__()
    else:
        if encoding:
            return bytes(item, encoding)
        else:
            return bytes(item)

def compat_chr(item):
    """Esta función es necesaria para mantener la compatibilidad
    entre Python 2.7 y 3.6. En Python 3.6, la función ``chr()``
    maneja cualquier caracter ``unicode``, mientras en 2.7,  ``chr()``
    sólo maneja los caraceteres ASCII.

    :param item: Cadena de 1 caracter de longitud cuyo método ``chr``
        necesita ser invocado.

    :return: El punto de código unichr de la cadena de un solo caracter.
    """
    if sys.version >= '3.0':
        return chr(item)
    else:
        return unichr(item)
