#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Esta función es recomendable incluirla en los
# decoradores porque el decorador externo toma
# el docstring de la función decorada, además
# por un tema de legibilidad del código:
from functools import wraps

# =========================================

###   Decorador simple   ###

def decorador(f):
    @wraps(f)
    def envuelto(*args, **kwargs):
        print("Antes de la función")
        resultado = f(*args, **kwargs)
        print("Después de la función")
        return resultado
    return envuelto

@decorador
def funcion(arg):
    print("Función, argumento: %s" % str(arg))
    return "Valor de retorno"

"""
>>> print(funcion(123))
Antes de la función
Función, argumento: 123
Después de la función
Valor de retorno
"""

# =========================================

### Decorador con argumentos   ###

def decorador_multiple(count):
    def decorador(f):
        @wraps(f)
        def envuelto(*args, **kwargs):
            for _ in range(count):
                print("Antes de la función")
            resultado = f(*args, **kwargs)
            for _ in range(count):
                print("Después de la función")
            return resultado
        return envuelto
    return decorador

@decorador_multiple(2)
def funcion(arg):
    print("Función, argumento: %s" % str(arg))
    return "Valor de retorno"

"""
>>> print(funcion(123))
Antes de la función
Antes de la función
Función, argumento: 123
Después de la función
Después de la función
Valor de retorno
"""