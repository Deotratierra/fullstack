#!/bin/bash

: '
    Busca dentro del directorio pasado como primer argumento
      (y en todos sus subdirectorios recursivamente) por archivos
      con la extensión pasada como segundo argumento e imprime
      la cantidad de ellos
'

find $1 -type f -name "*.$2" -printf x | wc -c

