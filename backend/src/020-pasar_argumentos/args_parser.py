#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys

# https://docs.python.org/3/library/argparse.html

# =======================================================================================

# Inicializar
parser = argparse.ArgumentParser(description="Descripción del programa",
	                             epilog="Descripción del programa después de los argumentos")

# ---------------------------------------------------------------------------------

# Introducir argumentos posicionales:
parser.add_argument("posicional", help="Argumento posicional")

# Introducir argumentos opcionales:
parser.add_argument("--opcional", "-o", help="Argumento opcional con valor.")

# Introducir flags verdadero/falso:
parser.add_argument("--debug", "-d", help="Mostrar mensajes de debug durante el script.",
	                dest="debug", action="store_false") # Por defecto False

# Pasar varios valores a un argumento (se guarda como lista)
parser.add_argument("--ports", "-p", help="Rango de puertos donde buscar los servicios.",
    	            nargs="+", type=int)

# --------------------------------------------------------------------------------------

# Parsear argumentos
args = parser.parse_args()

# Obtener un argumento posicional:
print(args.posicional)
#print(sys.argv[1])  # <--- Primer parámetro (sys.argv[0] es el nombre del archivo)

# Obtener un argumento opcional:
if args.verbose:
    print(args.verbose)

# =================================================================================

#####   VISIÓN GLOBAL DE PARÁMETROS   #####

print("Has introducido %d número de argumentos" % len(sys.argv))
print("Las variables referidas a los parámetros introducidos son: ", sys.argv)
print("El nombre del script es %s" % __file__)

# =================================================================================
