#!/bin/bash

# Debian

# Obtener la versión del sistema operativo
read -d . VERSION < /etc/debian_version
echo $VERSION  # Por ejemplo, en Debian stretch sería 9
# También así
VERSION=$(sed 's/\..*//' /etc/debian_version)



