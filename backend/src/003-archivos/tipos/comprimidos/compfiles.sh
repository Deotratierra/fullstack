#!/bin/bash

# ¡NO EJECUTAR"

# ----------------------------------------

# Comprimir un directorio en .tar.gz
tar -zcvf archivo.tar.gz directorio

# Parámetros:
#     -z  -->  Comprimir usando gzip
#     -c  -->  Crear archivo
#     -v  -->  Verbosidad
#     -f  -->  Nombre del archivo


# Descomprimir un archivo .tar.gz
tar -zxvf archivo.tar.gz

# ---------------------------------------

# Comprimir un directorio en .zip
zip -r directorio{.zip,}    # <-- Mismo nombre

zip -r archivo.zip directorio 


# Descomprimir un archivo .zip
unzip archivo.zip     # sudo apt-get install unzip

unzip archivo.zip -d directorio

# ---------------------------------------