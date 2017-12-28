#!/bin/bash

#####   VISIÓN GLOBAL DE PARÁMETROS   #####

echo "Has introducido $# número de argumentos"
echo "Los parámetros introducidos son: $*"
echo "El nombre del script es $0"
echo "El código de retorno del último comando es $?"

#####   VER PARÁMETROS INTRODUCIDOS   #####
echo "El parámetro \$1 es igual a $1"
echo "El parámetro \$2 es igual a $2"

# Para situaciones más complejas: getopt