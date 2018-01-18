#!/bin/bash

PS3='Elige una opción: '
opciones=("Opción 1" "Opción 2" "Opción 3" "Salir")
select opcion in "${opciones[@]}"
do
    case $opcion in
        "Opción 1")
            echo "Has elegido la opción 1"
            break
            ;;
        "Opción 2")
            echo "Has elegido la opción 2"
            break
            ;;
        "Opción 3")
            echo "Has elegido la opción 3"
            break
            ;;
        "Salir")
            echo "Hasta luego"
            break
            ;;
        *) echo Opción inválida;;
    esac
done
