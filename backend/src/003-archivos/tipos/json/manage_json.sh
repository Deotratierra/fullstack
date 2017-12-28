#!/bin/bash

# Crear archivos JSON
json_dict='{"clave1":"valor1","clave2":2}'

# Para parsear JSON en Bash es conveniente instalar jq
# sudo apt-get install jq

# Para mostrar JSON de forma leíble:
echo ${json_dict} | jq "."

# -----------------------------------------------------
     #     FILTROS      #

# Para saber el tipo de dato
echo ${json_dict} | jq type   # "object"

# Para saber la longitud
echo ${json_dict} | jq length  # 2

# -----------------------------------------------------

#     ACCESO A CLAVES Y VALORES      #

# Obtener las claves
echo ${json_dict} | jq 'keys'
# Obtener la primera clave
echo ${json_dict} | jq 'keys | .[0]'

# Obtener valores por clave
echo ${json_dict} | jq ".clave1"

# -----------------------------------------------------

# Podemos acceder a los valores por claves que concuerden con un valor,
# por valores que cumplan condiciones, editar JSON...
# ... y muchísimo más (consulta las fuentes)

# Fuentes:
# http://blog.librato.com/posts/jq-json
# https://shapeshed.com/jq-json/
# https://stedolan.github.io/jq/manual/
