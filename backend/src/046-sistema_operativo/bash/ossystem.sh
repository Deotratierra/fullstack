#!/bin/bash

# Obtener información sobre la versión de la distribución
cat /etc/os-release

echo


# Obtener el número de la versión de la distibución
# (válido en: {Ubuntu, Debian})
function osdist_version_number() {

  # ¿En qué versión estamos?
  local DIST=$(awk '/^ID=/' /etc/*-release | awk -F'=' '{ print tolower($2) }')

  case $DIST in
  debian)
    local VERSION_NUM=$(cat /etc/debian_version)
    ;;
  ubuntu)
    local VERSION_NUM=$(grep DISTRIB_RELEASE /etc/lsb-release | cut -d = -f 2)
    ;;
  esac

  echo "$VERSION_NUM"

}

VERSION_NUM=$(osdist_version_number)
echo $VERSION_NUM