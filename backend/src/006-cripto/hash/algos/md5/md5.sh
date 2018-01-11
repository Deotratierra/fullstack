#!/bin/bash

# Para generar resúmenes de un programa
# para validar la integridad de nuestro código podemos
# utilizar la herramienta md5sum en Linux:

# -------------------------------------------------------

# Generar el hash de un archivo
md5sum archivo.txt

# Generar el hash de varios archivos
md5sum archivo.txt README.md

# ------------------------------------------------

# Generar el hash de un archivo y guardarlo en otro junto a su nombre
md5sum archivo.txt > hash.md5  # Aquí lo guardamos

# Comparar el hash del archivo guardado por nombre con el propio archivo
# para comprobar si coincide o no
md5sum -c hash.md5   # Aquí lo comparamos

# ========================================================

# Fuentes:
# https://www.heatware.net/linux-unix/how-to-create-md5-checksums-and-validate-a-file-in-linux/
