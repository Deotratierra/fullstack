#!/bin/sh

# Obtener el sistema operativo
# en el que nos encontramos

# Nombre del sistema operativo:
uname -s  # uname  <-- También

# Tipo del sistema operativo:
echo $OSTYPE


# Diferentes sistemas operativos:
: '

if [[ "$OSTYPE" == "linux-gnu" ]]; then
        # ...
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
elif [[ "$OSTYPE" == "win32" ]]; then
        # Im not sure this can happen.
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        # ...
else
        # Desconocido.
fi

'
