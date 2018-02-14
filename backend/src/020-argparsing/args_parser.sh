#!/bin/bash

# =====================================================================

#####   VISIÓN GLOBAL DE PARÁMETROS   #####

echo "Has introducido $# número de argumentos"
echo "Los parámetros introducidos son: $*"
echo "El nombre del script es $0"
echo "El código de retorno del último comando es $?"

#####   VER PARÁMETROS INTRODUCIDOS   #####
echo "El parámetro \$1 es igual a $1"
echo "El parámetro \$2 es igual a $2"

echo
# ======================================================================

#####   PARSEAR ARGUMENTOS   #####
# El siguiente código parsea argumentos en la forma:
# -e "opcion" -a "otra_opcion" --flag --flag2 arg_posicional_1 arg_pos_2

# Array de argumentos posicionales
POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

: '
El comando shift toma un número como argumento opcional (1 por defecto)
y mueve los parámetros posicionales pasados al script ($*) a la izquierda
el número que se ha introducido en el comando, renombrándolos. Ejemplo:
shift   ->   de $3  pasa a $2,  de $2 pasa a $1... etc
'
case $key in
  -e|--extension)  # Así tomamos argumentos opcionales
  EXTENSION="$2"
  shift 2 # Los vamos renombrando
  ;;
  -s|--searchpath)
  SEARCHPATH="$2"
  shift 2
  ;;
  -l|--lib)
  LIBPATH="$2"
  shift 2
  ;;
  --default)
  DEFAULT=YES
  shift  # Sólo una vez si es del tipo booleano
  ;;
  *)    # Si es una opción desconocida es un argumento posicional
  POSITIONAL+=("$1") # Los vamos guardando en un array
  shift
  ;;
esac
done
set -- "${POSITIONAL[@]}" # Los parámetros posicionales ahora entran
                          # como primeros argumentos del script

echo FILE EXTENSION  = "${EXTENSION}"
echo SEARCH PATH     = "${SEARCHPATH}"
echo LIBRARY PATH    = "${LIBPATH}"
echo DEFAULT         = "${DEFAULT}"
echo "Número de archivos en el path de búsqueda con la extensión:" $(ls -1 "${SEARCHPATH}"/*."${EXTENSION}" | wc -l)
if [[ -n $1 ]]; then
    echo "Última línea del archivo específicado como argumento posicional:"
    tail -1 "$1"
fi

: '
Ejemplo de uso:  bash args_parser.sh -e sh -s . args_parser.py

FILE EXTENSION = sh
SEARCH PATH = .
LIBRARY PATH =
DEFAULT =
Número de archivos en el path de búsqueda con la extensión: 1
Última línea del archivo específicado como argumento posicional:
# ====================================================================
'

# ===========================================================================


# Imprime la ayuda de un script invocado desde línea de comandos
# El texto de información debe estar guardado en la variable $usage
function help () {
  echo "" 1>&2
  input "   $@" 1>&2
  if [ -n "${usage}" ]; then # Imprime la información de $usage si está disponible
    echo "   ${usage}" 1>&2
  fi
  echo "" 1>&2
  exit 1
}
