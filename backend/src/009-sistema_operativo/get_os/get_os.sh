#!/bin/sh

# ===================================================================
#     Obtener el sistema operativo en el que nos encontramos

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
  echo "No tengo ni idea de donde estamos, pero quizá esto te ayude: $OSTYPE"
fi

# =======================================================================

#             Obtener la versión de cada sistema operativo

# -----------------------------------------------------------------------
#                             MACOSX

sysctl kern.osrelease

: '
Correspondencia de las versiones del sistema operativo
con el lanzamiento de la versión OSX

16.x.x  macOS 10.12.x Sierra
15.x.x  OS X  10.11.x El Capitan
14.x.x  OS X  10.10.x Yosemite
13.x.x  OS X  10.9.x  Mavericks
12.x.x  OS X  10.8.x  Mountain Lion
11.x.x  OS X  10.7.x  Lion
10.x.x  OS X  10.6.x  Snow Leopard
 9.x.x  OS X  10.5.x  Leopard
 8.x.x  OS X  10.4.x  Tiger
 7.x.x  OS X  10.3.x  Panther
 6.x.x  OS X  10.2.x  Jaguar
 5.x    OS X  10.1.x  Puma
'

# -----------------------------------------------------------------------


# =======================================================================
