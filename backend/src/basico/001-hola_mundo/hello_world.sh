#!/bin/bash

main()
{
    echo "¡Hola mundo en Bash!"

    # Caracter de escape: \
    echo \
        "¡Hola mundo escapando a la siguiente línea en Bash!"
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi

# ============================================

# Comentarios de una línea

: '
Comentarios de
varias líneas
'