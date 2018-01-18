#!/bin/bash

# Obtener información sobre la versión de la distribución
cat /etc/os-release

echo


# Obtener el número de la versión de la distibución
# (válido en: {Ubuntu, Debian})
function osdist_version() {

  # ¿En qué versión estamos?
  local DIST=$(awk '/^ID=/' /etc/os-release | awk -F'=' '{ print tolower($2) }')

  # Dependiendo de la versión, el comando para saber su número varía
  case $DIST in
  debian)
    local DIST_VERSION=$(cat /etc/debian_version)
    ;;
  ubuntu)
    local DIST_VERSION=$(grep DISTRIB_RELEASE /etc/lsb-release | cut -d = -f 2)
    ;;
  '"centos"')
    local DIST_VERSION=$(cat /etc/centos-release | cut -d " " -f 4)
    ;;
  esac

  echo "$DIST_VERSION"

}

VERSION_NUM=$(osdist_version)
echo $VERSION_NUM