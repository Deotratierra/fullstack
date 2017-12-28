#!/bin/bash

# ---   Crear un archivo en un archivo   ---
# Vacío
touch ejemplo.txt

# Escribiendo en él
echo "Contenido del archivo" > ejemplo.txt

# ---   Imprimir el contenido de un fichero   ---

# Opción 1
cat fichero.txt

echo

# Opción 2
echo "$(<fichero.txt)"

echo

# Las primeras líneas
head fichero.txt

echo

# Las últimas líneas:
tail fichero.txt

echo

echo "==========================================="
# ==================================================

# ---   Obtener el contenido de un fichero   ---

# Opción 1
content=$(cat fichero.txt)
echo $content

echo

# Opción 2
content="$(<fichero.txt)"
echo "$content"