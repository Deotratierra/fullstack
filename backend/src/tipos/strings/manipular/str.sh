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

#######     Funciones útiles     #######

# Convierte texto a minúscula.
# Formas de uso:  text=$(lower <<<"$1")
#                 echo "MAKETHISLOWERCASE" | lower
lower() { tr '[:upper:]' '[:lower:]' }

# Convierte texto a mayúscula.
# Formas de uso:  text=$(upper <<<"$1")
#                 echo "MAKETHISUPPERCASE" | upper
upper() { tr '[:lower:]' '[:upper:]' }

# -----------------------------------------------

# Elimina los espacios a la izquierda de la cadena.
ltrim() {
  local char=${1:-[:space:]}
  sed "s%^[${char//%/\\%}]*%%"
}

# Elimina los espacios a la derecha de la cadena.
rtrim() {
  local char=${1:-[:space:]}
  sed "s%[${char//%/\\%}]*$%%"
}

# Elimina los espacios a la derecha y a la izquierda de la cadena
# Ejemplo de uso:
#     echo "  foo  bar baz " | trim  #==> "foo  bar baz"
trim() {  ltrim "$1" | rtrim "$1" }

# Elimina los espacios a la izquierda y derecha de la cadena
# y unifica los espacios consecutivos por medio a uno solo.
#
# Ejemplo de uso:
#     echo "  foo  bar   baz  " | squeeze  #==> "foo bar baz"
squeeze() {
  local char=${1:-[[:space:]]}
  sed "s%\(${char//%/\\%}\)\+%\1%g" | trim "$char"
}

# Elimina las líneas en blanco al principio y al final de un documento
# y unifica las líneas consecutivas por medio a una sola.
squeeze_lines() {
  sed '/^[[:space:]]\+$/s/.*//g' | cat -s | trim_lines
}

# ==================================================================
