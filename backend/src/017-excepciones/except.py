#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lista de excepciones estándar
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions

import sys
import traceback  # https://docs.python.org/3/library/traceback.html

# =================================================================

# Cazar una excepción
try:
    response = 1/0
except ZeroDivisionError as error:
    print("No puedes dividir entre 0 o te saldrá el siguiente error:")
    print(error)
    # Podemos acceder a la información de la excepción de varias formas:
    # Python2
    ex_type, ex, tb = sys.exc_info()
    traceback.print_tb(tb)   # Traceback
    print(ex_type)           # Tipo de la excepción

    # Python 2/3
    print(error.__traceback__)  # Objeto traceback
    print("\n")

# Lanzar una excepción
try:
    raise KeyboardInterrupt
except:  # Cazar cualquier excepción (también vale except Exception:)
    pass
finally: # La cláusula finally es ejecutada siempre
    print("Seguimos la ejecución")

# Cazar varias excepciones
try:
    raise RuntimeError
except (RuntimeError, TypeError, ValueError):
    pass

# =================================================================

# Crear excepciones personalizadas:

class Error(Exception):
    """Clase base para las excepciones de este módulo"""
    pass

class FatalError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

raise FatalError("Expresión del error", "Mensaje de error")

# =================================================================