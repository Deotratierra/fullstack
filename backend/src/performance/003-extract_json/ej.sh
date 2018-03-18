#!/bin/sh

STRING='{"clave": "valor 1", "num": 2}'

function ej() {
    result=$(echo $STRING | jq ".[$1]" 2>&1)
    #echo $result
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    ej
fi


# Necesitas instalar jq para ejecutar este script:
# -------------------------------------------------
# curl http://stedolan.github.io/jq/download/linux64/jq -o ~/bin_compciv/jq
# chmod a+x ~/bin_compciv/jq
# -------------------------------------------------