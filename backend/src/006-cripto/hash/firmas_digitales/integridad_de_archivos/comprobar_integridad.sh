#!/bin/bash

# Para ejecutar este ejemplo necesitamos OpenSSL

# ----------------------------------------------

echo

# Creamos un hash de nuestro código fuente
echo "Creamos un hash MD5 del código"
HASH=$(cat lib/codigo_fuente.py | md5sum)
echo $HASH

echo
echo "-----> Hackeamos el código"
python3 hack_script.py

echo
echo "Volvemos a hashear el código fuente para comprobar si ha sido hackeado:"
HASH2=$(cat lib/codigo_fuente.py | md5sum)
echo $HASH2

# Si los hashes no coinciden es que el código ha cambiado
if [ "$HASH" != "$HASH2" ];
then
  echo "ATENCIÓN: ¡El código ha sido hackeado!"
else
  echo "Tu código está libre de infecciones"
fi

