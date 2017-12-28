#!/bin/bash

CURRENT_DIR=${PWD##*/}
if [ $CURRENT_DIR = "stats" ];
then
  cd ..
fi
CURRENT_DIR=${PWD##*/}
if [ $CURRENT_DIR = "scripts" ];
then
  cd ..
fi

# Cuantos archivos hay de cada lenguaje de backend
PY=$(bash scripts/stats/file_types.sh backend/src py)
IPYNB=$(bash scripts/stats/file_types.sh backend/src ipynb)
JS=$(bash scripts/stats/file_types.sh backend/src js)
RB=$(bash scripts/stats/file_types.sh backend/src rb)
CPP=$(bash scripts/stats/file_types.sh backend/src cpp)
SH=$(bash scripts/stats/file_types.sh backend/src sh)
TEX=$(bash scripts/stats/file_types.sh backend/src tex)

# Lo sacamos en JSON
printf '{"py":%d,"ipynb":%d,"js":%s,"rb":%s,"cpp":%s,"sh":%s,"tex":%s}' $PY $IPYNB "$JS" "$RB" "$CPP" "$SH" "$TEX"
