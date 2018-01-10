#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# El siguiente programa es una envoltura de pwgen
# (para las opciones ver el ejemplo en bash)

# NOTA: Cuidado porque a partir de 30 caracteres la
# generación se convierte exponencialmente ineficiente

from pwgen import pwgen  # pip3 install pwgen
from pprint import pprint

# 5 contraseñas sin símbolos ni ambigüedad
passwords = pwgen(43, 1, no_symbols=True, no_ambiguous=True)
pprint(passwords)  # Las retorna en una lista

# Código fuente: https://github.com/vinces1979/pwgen
