#!/bin/sh

# Debes editar a tu gusto añadir las siguientes líneas
# al archivo ~/.profile o algún otro que configure
# las siguientes variables de entorno al iniciar el tuyo:
:'
export GOROOT="/usr/local/go"
export GOPATH="$HOME/go"
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
'


# Debes editar las siguientes variables para establecer
# las rutas de tu instalación

INSTALL_DIR="/usr/local/go"   # Directorio de instalación
WORK_DIR="$HOME/go"           # Directorio de trabajo

# Script de descarga y almacenamiento del código fuente
wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz
tar -xvf go1.10.linux-amd64.tar.gz
rm go1.10.linux-amd64.tar.gz
sudo mv go $INSTALL_DIR
GOLANG_VERSION=$(`go version`)

if [ $? -eq 0 ]; then
  echo "$GOLANG_VERSION se ha instalado correctamente."
else
  echo "Ocurrió un error instalando Golang."
  echo "Asegúrate de haber establecido las variables de entorno necesarias antes de ejecutar el script."
fi
