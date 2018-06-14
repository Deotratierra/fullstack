#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================

# Saber de que tipo es una variable
print(type("hola"))   # <type 'str'>
#print(type(if))      # SyntaxError: invalid syntax
print(type(type))     # <type 'type'>

# Saber si una variable hereda de un tipo concreto
print(isinstance("hola", str))             # True
print(isinstance( "hola", (int, float) ))  # False

# ========================================
