#!/bin/bash

# Para obtener la versión del kernel en Linux:
uname -r


# Función para comprobar si la versión del Kernel
# del sistena operativo es superior a una versión
# pasada como primer argumento de la forma A.B.C-D
# https://es.wikipedia.org/wiki/N%C3%BAcleo_Linux
#
# Guarda 0 en la variable ALMOST si la versión del
# núcleo es menor a la pasada como argumento,
# 1 en caso contrario. Si ambas versiones son iguales
# también guarda 1
function kernel_almost() {

  # Required version splitted
  REQUIRED_VERSION=$1
  req_split=$(echo $REQUIRED_VERSION | tr "." "\n")
  set ${req_split[0]}
  reqA=$1
  reqB=$2
  reqC=$3
  reqC_split=$(echo $reqC | tr "-" "\n")
  set ${reqC_split[0]}
  reqC=$1
  reqD=$2
  if [ -z $reqD ]; then
    reqD=0
  fi


  # Kernel version splitted
  KERNEL_VERSION=(`uname -r`)
  kern_split=$(echo $KERNEL_VERSION | tr "." "\n")
  set ${kern_split[0]}
  kernA=$1
  kernB=$2
  kernC=$3
  kernC_split=$(echo $kernC | tr "-" "\n")
  set ${kernC_split[0]}
  kernC=$1
  kernD=$2
  if [ -z $kernD ]; then
    kernD=0
  fi

  ALMOST=0
  if [ $kernA -gt $reqA ]; then   # Kernel greater than required
    ALMOST=1
  else
    if [ $kernB -gt $reqB ]; then
      ALMOST=1
    else
      if [ $kernC -gt $reqC ]; then
        ALMOST=1
      else
        if [[ $kernD -gt $reqD || $kernD -eq $reqD ]]; then
          ALMOST=1
        fi
      fi
    fi
  fi
}

kernel_almost 4.9.0
echo $ALMOST