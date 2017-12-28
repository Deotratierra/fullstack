#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import colorama     # pip3 install colorama
# https://pypi.python.org/pypi/colorama
from colorama import Fore, Back, Style  # Frontal, de fondo, estilo

# Volver al color por defecto después de cada salida 
colorama.init(autoreset=True) 

# Consultar los colores y estilos disponibles:
for titulo, consulta in ( ("Colores", Fore), ("Estilos", Style) ):
    print("-----  %s  -----" % titulo)
    for elem in dir(consulta):
        if "__" not in elem and "RESET" not in elem:
            print(elem)
    print("============================")

# Aplicar color
print(Fore.LIGHTYELLOW_EX + "Texto amarillo")
print(Fore.MAGENTA + "Texto magenta")

# Aplicar color de fondo
msg = "Texto azul con fondo blanco"
print(Fore.LIGHTBLUE_EX + Back.LIGHTWHITE_EX + msg)

# Aplicar estilo
print(Style.BRIGHT + "Texto en negrita")