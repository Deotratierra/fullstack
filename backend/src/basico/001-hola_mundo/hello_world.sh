#!/bin/bash

main()
{
    echo "Hola mundo en Bash!"

    # Caracter de escape: \
    echo \
        "¡Hola mundo escapando a la siguiente línea en Bash!"
}

main "$@"

# Comentarios de una línea

: '
Comentarios de
varias líneas
'