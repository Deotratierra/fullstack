#!/bin/bash

# Introducir una contraseña sin mostrarla
echo "Introduce tu contraseña: "
read -s PASSWORD
echo $PASSWORD

echo
# ----------------------------------------------

# Introducir una contraseña mostrando asteriscos

echo "Introduce tu contraseña: "
password=""
while IFS= read -r -s -n1 pass; do
  if [ -z "$pass" ]; then
     echo
     break
  else
     printf "*"
     password="$password$pass"
  fi
done

# Fuente:
# https://stackoverflow.com/questions/4316730/linux-scripting-hiding-user-input-on-terminal
