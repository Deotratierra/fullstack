#!/usr/bin/sh

# Pasa como primer parámetro una dirección a la que enviar
# la petición POST. Por ejempo ejecuta:
# bash test.sh http://85.137.57.245:8001/log

curl -d "id=hola hola probando" -X POST $1