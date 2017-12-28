#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Referencia: https://docs.python.org/3.6/library/re.html

import re

texto = """Las expresiones regulares en Python se representan
con un carácter r delante de una cadena: """

expresion = r".a.."

# --------------------------------------------------

# Compilar expresiones regulares
patron = re.compile(expresion)
# https://docs.python.org/3.6/library/re.html#regular-expression-objects

# --------------------------------------------------

# Buscar todas las coincidencias (ejemplo compilando):
coincidencias = patron.findall(texto) # ['Las ', 'lare', 'cará', 'lant', 'na c']

# Ejemplo sin compilar:
coincidencias = re.findall(expresion, texto)

# --------------------------------------------------

# Buscar si hay coincidencias
coincidencia = re.search(expresion, texto) # <_sre.SRE_Match object; span=(1, 5), match='Las '>

# Retorna un objeto Match con la primera coincidencia si la hay o None si no
# https://docs.python.org/3.6/library/re.html#match-objects

# --------------------------------------------------

# Buscar coincidencia al principio de la cadena
coincidencia_al_principio = re.match(expresion, texto) # <_sre.SRE_Match object; span=(0, 4), match='Las '>

# Buscar coincidencia completa
coincidencia_completa = re.fullmatch(expresion, texto) # None

# --------------------------------------------------

# Substituir cadenas
substitucion = re.sub(expresion, "...", texto) # ...expresiones regu...s en Python se representan
                                               # con un ...cter r de...e de u...adena:

# --------------------------------------------------
