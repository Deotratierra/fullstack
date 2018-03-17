#!/bin/sh


function rs() {
    for i in $(seq 1 $1); do
	    string="Salida de emergencia"
	    pattern="Salida"
	    substitution="Entrada"
	    result=("${string//$pattern/$substitution}")
	done
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    rs $1
fi
