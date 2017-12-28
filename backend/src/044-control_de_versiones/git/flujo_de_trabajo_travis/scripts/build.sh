#!/bin/bash

# Si ejecutamos build.sh desde el directorio scripts
CURRENT_DIR=${PWD##*/}
if [ $CURRENT_DIR = "scripts" ];
then
  cd ..  # salimos a la raíz del proyecto
  CURRENT_DIR=${PWD##*/}
else  # Pero si lo ejecutamos desde otro lugar
  if ! [ -d "scripts" ]; # comprobamos si no existe el directorio
  then  # lo cual indica que no estamos en la raíz
    echo "Por favor, ejecuta el script desde la raíz del proyecto"
    exit 1
  fi
fi

# Ejecutamos los tests unitarios
# (personalizar y descomentar las siguientes líneas):
: '
python3 tests/tests.py
if [ $? -gt 0 ];
then
  exit 1
fi
'





