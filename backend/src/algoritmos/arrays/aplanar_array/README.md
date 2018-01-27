### Problema
Dado un array que contiene arrays anidados, obtener un sólo array.

Input:  [2, 1, [3, [4, 5], 6], 7, [8]]

Output: [2, 1, 3, 4, 5, 6, 7, 8]

______________________

### Explicación

El truco de este algoritmo es la recursividad interna.

Lo primero que hace es crear un array vacío si no le proveemos de uno pasándolo como parámetro opcional.
Entonces va iterando por cada elemento del array que queremos aplanar, y, si el elemento que encuentra no es un array lo agrega al array que ha inicializado al principio. En caso de que el elemento sea un array, introduce el array que está fabricando como el array fuente en una nueva llamada interna e itera por el que ha encontrado, forzando a encadenarlo todo al array fuente.

> Fuente: https://github.com/keon/algorithms/blob/master/array/flatten.py