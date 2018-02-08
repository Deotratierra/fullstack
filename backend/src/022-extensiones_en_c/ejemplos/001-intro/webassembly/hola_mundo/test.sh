#!/bin/sh

# Compila
emcc hola.c -s WASM=1 -o hola.html

# Lanza un pequeño servidor
python -m SimpleHTTPServer 8765

# Limpia el directorio
rm hola.html hola.js hola.wasm
