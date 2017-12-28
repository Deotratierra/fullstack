#!/bin/bash

main(){
    # Si el primer parámetro es mayor o igual que el segundo...
    if [ $1 -ge $2 ]; then 
        return $1;
    else
        return $2;
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main 3 5
    echo $? # Imprimir el valor la última variable utilizada
fi
