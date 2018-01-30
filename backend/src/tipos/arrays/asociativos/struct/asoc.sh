#!/bin/bash


# La versión de Bash debe ser al menos la 4 para usar arrays asociativos
bash --version

# =====================================================================

: '
La opción -A declara a la variable que la sigue como un array asociativo.
'
# Declarar por partes
declare -A diccionario_1
diccionario_1["clave_1"]="valor 1"
diccionario_1["clave_2"]="valor 2"

# Declarar directamente
declare -A diccionario_2=( ["clave con espacios"]="valor 3" )
# Las claves pueden contener espacios

# =====================================================================

# Obtener valores
echo ${diccionario_1[clave_1]}  # valor 1

VALOR_3=${diccionario_2[clave con espacios]}
echo $VALOR_3                   # valor 3

# =====================================================================

# Iterar
for key in "${!diccionario_1[@]}";
do
   echo ${diccionario_1[$key]}    # valor 1
done                              # valor 2

# =====================================================================

# Eliminar array asociativo
unset diccionario_2

# Eliminar claves
unset diccionario_1["clave_2"]

# =====================================================================

# Obtener el largo
echo ${#diccionario_1[@]}  # 1

# Obtener las claves
KEYS=(${!diccionario_1[@]})

# ======================================================================
