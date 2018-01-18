#!/bin/bash

INVALIDA=1
while [ $INVALIDA -eq 1 ]; do
  read -p "¿Quieres instalar el programa? S/N: " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Ss]$ ]]; then
    echo "Instalando..."
    INVALIDA=0
  elif [[ $REPLY =~ ^[Nn]$ ]]; then
    echo "Lo dejaremos sin instalar."
    INVALIDA=0
  else
    echo "Opción inválida"
    echo
  fi
done


# ===============================================

: '
Fuentes:
https://stackoverflow.com/questions/1885525/how-do-i-prompt-a-user-for-confirmation-in-bash-script
'