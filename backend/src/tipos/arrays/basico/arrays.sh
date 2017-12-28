#!/bin/bash

# Es importante no confundir un array
# con una lista:
# array=(elem1, elem2, elem3)
# lista={array[*]}

# Los bucles for sólo encontrarán un elemento
# en un array, para recorrerlos debemos
# convertirlo en lista.

# =====================================

# Declarar arrays
array=( a b c d e f g h i j )
declare -a array2=(1 2 3)


# Acceder al array completo
echo ${array[*]}   #  a b c d e f g h i j
echo ${array2[@]}  #  1 2 3

# Acceder a un elemento del array
echo ${array[1]}   #  b
echo ${array2[10]} #  Esto aparece vacío
# (bash no comprueba los límites del array)

# Agregar un elemento al array
array2[11]=4
echo ${array2[*]}  #  1 2 3 4

# Acceder a los índices de los elementos
echo ${!array2[*]} #  0 1 2 11

# Acceder al número de elementos
echo ${#array2[*]} #  4

# Rangos
array3=( {5..10} )
echo ${array3[*]}  #  5 6 7 8 9 10


# Recorrer un array
for i in ${array3[*]}; do
    echo $i
done

for i in {15..20}; do
    echo $i
done

# Para salir de un array usamos break

# Otra forma de bucle:
for (( i=1; i<=5; i++)); do
    echo "Ciclo $i"
done


# =========================================

# Ejemplo: lista de archivos en un array

ficheros=`ls`
echo ${ficheros[*]}

for fichero in ${ficheros[*]}; do
    echo $fichero
    break
done
