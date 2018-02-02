#!/bin/bash

# ==============================================
#                   ARCHIVOS

# Crear archivo vacío
touch archivo.txt

# Crear archivo añadiendo texto
echo "Texto a volcar" > archivo2.txt

# Mover o renombrar archivos
mv archivo.txt archivo1.txt

# Copiar archivos
cp archivo2.txt archivo3.txt

# Borrar archivos
rm archivo1.txt archivo2.txt archivo3.txt

# ----------------------------------------------

# Mostrar todos los archivos del directorio actual
ls    # También con (ver globs):
echo *

# Obtener el nombre del archivo actual
archivo_actual=${0}

# Mostrar archivos ocultos
ls -ld .?*

# Eliminar archivos en subdirectorios mediante expresión regular
find . -type f -name "<expresión>" -delete

# Eliminar directorios en subdirectorios mediante expresión regular:
find -name "<expresión>" -exec rm -rf {} \;

# ==============================================


# ==============================================
#                 DIRECTORIOS

# Obtener la ruta completa actual
$PWD

# Obtener el directorio actual
echo ${PWD##*/}

# Crear directorio
mkdir directorio directorio2

# Crear jerarquía de directorios
mkdir -p directorio/otro/mas_profundo

# Borrar directorio
rmdir directorio

# Borrar directorio y su contenido recursivamente
rm -Rf directorio2

# ==============================================


# =============================================
#                  RUTAS

# Obtener el path completo de un archivo
readlink -f $archivo_actual

# Obtener la base de una ruta
basename $PWD

# ==============================================