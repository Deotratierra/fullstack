#!/bin/bash

# Ejecutar un script desde url
SCRIPT_URL="https://gist.githubusercontent.com/mondeja/2df93881bff3e800b9282393ea1dbeb7/raw/78521789438ffef714f32e3d2a76aeb4df4dca92"
curl -s $SCRIPT_URL | bash

# Podemos pasarle comandos después de "bash"
