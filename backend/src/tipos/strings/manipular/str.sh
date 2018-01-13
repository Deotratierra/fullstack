#!/bin/bash

# Reemplazar todos los caracteres por otro (no funciona con unicode)
echo "HOLA QUE TAL" | tr "HLO" "h"  # hhhA QUE TAh
SALIDA=$(echo "HOLA" | tr "LO" "AEA")  # Se cambia "O" por "E" y "L" por "A"
echo $SALIDA # HALA
# El comportamiento de tr no es muy intuitivo:
# https://es.wikipedia.org/wiki/Tr_(Unix)

# ==================================================================

# sed
# Este comando permite modificar el flujo de cadenas o las lineas de un archivo

# Permite modificaciones muy complejas por expresiones regulares,
# sustitución, inserción, eliminación, visualización, etc:
# Usa expresiones regulares básicas: https://en.wikipedia.org/wiki/Regular_expression#POSIX_basic_and_extended

# Básico: https://enavas.blogspot.com.es/2008/03/el-shell-de-linux-comando-sed.html
# Manual completo: https://www.gnu.org/software/sed/manual/sed.html

# ---------------------------------

# El uso más simple es obtener una línea de un archivo por expresión regular
sed -n '/std/p' str.cpp   # using namespace std;


# ==================================================================
