#!/bin/bash

# ===============================================

# Función de selección sí o no
# Toma una pregunta como primer argumento
# Guarda la respuesta (S/N) en la variable $SELEC
function selec_si_no() {
  INVALIDA=1
  while [ $INVALIDA -eq 1 ]; do
    INVALIDA=0
    read -p "$1" -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then    # SI
      SELEC="S"
    elif [[ $REPLY =~ ^[Nn]$ ]]; then  # NO
      SELEC="N"
    else
      echo "Opción inválida"
      echo
      INVALIDA=1
    fi
  done
}

selec_si_no "¿Quieres instalar el programa? S/N: "

if [[ $SELEC == "S" ]]; then
  echo "Instalando..."
else
  echo "Abortando instalación..."
fi


# ===============================================
# In english for easy introduction in you projects

# Selection function yes/no
# Pass a question as first argument
# Then check the answer (Y/N) on $SELEC variable
function select_yes_no() {
  invalid=1
  while [ $invalid -eq 1 ]; do
    invalid=0
    read -p "$1" -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then    # YES
      SELEC="Y"
    elif [[ $REPLY =~ ^[Nn]$ ]]; then  # NO
      SELEC="N"
    else
      echo "Invalid option"
      echo
      invalid=1
    fi
  done
}

selec_si_no "Do you want to install the program? Y/N: "

if [[ $SELEC == "Y" ]]; then
  echo "Installing..."
else
  echo "Aborting install..."
fi

# ===============================================

: '
Fuentes:
https://stackoverflow.com/questions/1885525/how-do-i-prompt-a-user-for-confirmation-in-bash-script
'
