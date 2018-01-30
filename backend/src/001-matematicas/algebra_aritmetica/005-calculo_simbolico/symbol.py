#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================== Sympy ===========================
# http://www.sympy.org

""" El alma del Cálculo Simbólico son las variables simbólicas,
que en SymPy son instancias de la clase Symbol: """

from pprint import pprint
from sympy import Symbol, symbols

# Definir un símbolo
x = Symbol("x")

# Definir varios símbolos
a, b, c = symbols("a", "b", "c")

# Al definir una variable podemos hacer suposiciones sobre ella:
y = Symbol("y", real=True)


""" Fuentes:
http://www.pybonacci.org/2012/04/04/introduccion-al-calculo-simbolico-en-python-con-sympy/
"""
