#!/bin/bash

: '
MacOSX está basado en LinuxBSD, por lo tanto sus sistemas gestores de paquetes
se parecen bastante a los de Linux.

En MacOSX, existen 3 gestores de paquetes principales: MacPorts, Flink y Homebrew.
Aquí sólo cubriremos Homebrew por su facilidad respecto a los otros.
'

# ==========================================================================
#                                HOMEBREW
# https://brew.sh/index_es.html

# Instalación:
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# -----------------------------------

# Instalar paquetes
    # Homebrew
brew install <paquete>
    # Mediante un archivo .pkg
sudo installer -pkg ruta/al/archivo.pkg -target /

# Listar los paquetes instalados
brew ls

# Actualizar paquete
brew upgrade <paquete>
# Actualizar todos los paquetes
brew upgrade

# Desinstalar paquete
brew install <paquete>


# Comprobar si un paquete está instalado
brew ls --versions <paquete> # Si lo está imprime las versiones

if brew ls --versions <paquete> > /dev/null; then
  echo "El paquete <paquete> está instalado."
else
  echo "El paquete <paquete> no está instalado."
fi


# ==========================================================================
