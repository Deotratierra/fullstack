#!/bin/bash

# Debemos ejecutar las bibliotecas para acceder
# a sus funciones y las variables
. modulo.sh
# También vale así:
source modulo.sh

funcion_en_modulo
echo $VARIABLE
