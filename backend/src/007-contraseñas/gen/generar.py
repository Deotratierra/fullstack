#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# El siguiente programa es una envoltura de pwgen
# (para las opciones ver el ejemplo en bash)

from pwgen import pwgen  # pip3 install pwgen
from pprint import pprint

# 5 contraseñas sin símbolos ni ambigüedad
passwords = pwgen(20, 1, no_symbols=True, no_ambiguous=True)
pprint(passwords)  # Las retorna en una lista

# Código fuente: https://github.com/vinces1979/pwgen

# ==========================================================

# NOTA: Cuidado porque a partir de 30 caracteres la
# generación se convierte exponencialmente ineficiente
# (lo que no sucede con la versión pwgen de Bash)

from timeit import timeit

for i in range(30, 37):
    spent = timeit("pwgen(%d, 1, no_symbols=True, no_ambiguous=True)" % i,
    	           setup="from pwgen import pwgen", number=5)
    print("Time spent for a password of %d characters: %f" % (i, spent))
