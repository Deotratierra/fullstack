#!/bin/bash

# Obtener información sobre la versión de la distribución
#cat /etc/os-release

#echo


# Obtener el número de la versión de la distibución
# (válido en: {Ubuntu, Debian, CentOs})
# Obtén el nombre de la distribución en la variable $DIST
# y la versión de la misma en la variable $DIST_VERSION
function osdist_version() {

  DIST="$(. /etc/os-release && echo "$ID")"

  # Dependiendo de la versión, el comando para saber su número varía
  case $DIST in
  debian)
    DIST_VERSION=$(grep -e '.*' /etc/debian_version)
    ;;
  ubuntu)
    DIST_VERSION=$(grep DISTRIB_RELEASE /etc/lsb-release | cut -d = -f 2)
    ;;
  '"centos"')
    DIST_VERSION=$(cat /etc/centos-release | cut -d " " -f 4)
    ;;
  esac

}

osdist_version
echo $DIST $DIST_VERSION