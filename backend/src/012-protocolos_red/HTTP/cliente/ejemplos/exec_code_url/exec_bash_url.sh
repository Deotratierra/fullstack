#!/bin/bash

# ===================================================
#          Ejecutar un script desde url

SCRIPT_URL="URL"

# curl
curl -s $SCRIPT_URL | bash

# *Podemos pasarle comandos después de "bash"

# ----------------------------------------------

# wget
wget $SCRIPT_URL && bash install.sh

# ===================================================
