### Problema

Hay un parking con un solo espacio vacío. Nos dan la disposición inicial de los coches y el estado final en el que deben quedar. En cada paso sólo está permitido mover un coche fuera de su plaza hacia el aparcamiento vacío.
El objetivo es encontrar el menor movimiento necesario para reorganizar el parking desde el estado inicial al final.

Digamos que el estado inicial es un array `[1, 2, 3, 0, 4]` y el estado final es `[0, 3, 2, 1, 4]`. 
Podemos intercambiar el 1 con el 0 en el array inicial y así sucesivamente. 

___________________________________________________

### Explicación

Veamos el ejemplo, que se resuelve en 4 movimientos, paso por paso:

1º Se cambia el 1 por el 0: `[0, 2, 3, 1, 4]`
2º Se cambia el 0 por el 2: `[2, 0, 3, 1, 4]`
3º Se cambia el 3 por el 0: `[2, 3, 0, 1, 4]`
4º Se cambia el 2 por el 0: `[0, 3, 2, 1, 4]`

Si observamos el algoritmo, que está comentado en el caso de Python, veremos que lo que intenta es poner al 0 en su posición final. A partir de ahí vamos comprobando los números que no están en su posición y los vamos cambiando por el 0 hasta que obtenemos el array final.




>Fuente: https://github.com/keon/algorithms/blob/master/array/garage.py