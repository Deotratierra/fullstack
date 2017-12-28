#!/bin/bash

num1=4511
num2=369301

function digits_sum {
	local number=$1    # Recibimos el argumento de la función
	local total=0
	response=""
    while [ $number -ne 0 ]; do # While number not equal to zero
        (( rest = $number % 10 )) # Comando compuesto artimético
        response=$response$rest
        (( total = $total + $rest ))
        (( number = $number / 10))
        if (( number > 0 )); then
            response=$response" + "
        fi
    done
    response=$response" = "$total
}

digits_sum $num1
echo $response

digits_sum $num2
echo $response

# Fuente:
# http://wiki.bash-hackers.org/commands/builtin/let