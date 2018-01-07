#!/bin/bash

# Obtener información sobre la versión de la distribución
cat /etc/os-release

echo


# Obtener el número de la versión de la distibución
# (válido en: {Ubuntu, Debian})
function osdist_version_number() {

  # ¿En qué versión estamos?
  local DIST=$(awk '/^ID=/' /etc/os-release | awk -F'=' '{ print tolower($2) }')

  # Dependiendo de la versión, el comando para saber su número varía
  case $DIST in
  debian)
    local VERSION_NUM=$(cat /etc/debian_version)
    ;;
  ubuntu)
    local VERSION_NUM=$(grep DISTRIB_RELEASE /etc/lsb-release | cut -d = -f 2)
    ;;
  '"centos"')
    local VERSION_NUM=$(cat /etc/centos-release | cut -d " " -f 4)
    ;;
  esac

  echo "$VERSION_NUM"

}

VERSION_NUM=$(osdist_version_number)
echo $VERSION_NUM