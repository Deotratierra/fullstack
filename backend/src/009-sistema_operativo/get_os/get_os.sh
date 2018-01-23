#!/bin/sh

# Obtener el sistema operativo
# en el que nos encontramos

# Nombre del sistema operativo:
uname -s  # uname  <-- También

# Tipo del sistema operativo:
echo $OSTYPE


# Diferentes sistemas operativos:
echo "¿En qué sistema operativo estamos?"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "Estamos en Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Estamos en Mac OSX"
elif [[ "$OSTYPE" == "cygwin" ]]; then
  echo "Estamos en CygWin"
  # https://es.wikipedia.org/wiki/Cygwin
elif [[ "$OSTYPE" == "msys" ]]; then
  echo "Estamos en MinGW"
  # https://es.wikipedia.org/wiki/MinGW
elif [[ "$OSTYPE" == "win32" ]]; then
  echo "Estamos en Windows32 (¿Esto es posible?)"
elif [[ "$OSTYPE" == "freebsd"* ]]; then
  echo "Estams en FreeBSD"
else
  echo "No tengo ni idea de donde estamos, pero quizá esto te ayude: "
  echo $OSTYPE
fi


