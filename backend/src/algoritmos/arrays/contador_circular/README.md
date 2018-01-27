### Problema
Imagina a un grupo de gente sentada en círculo,
debes coger uno cada x miembros y sacarlo del círculo.
Luego empiezas a contar desde el miembro que has sacado.
Repite la operación hasta que no queda nadie en el círculo

Por ejemplo:

Input: 123456789

  --> Salto = 3

Output: 369485271

___________________________________

### Explicación

El truco del algoritmo está en la línea `idx = (skip + idx) % len(int_list)`. Para comprenderlo a través del ejemplo de arriba:

skip = 2
- 1ª Iteración:
`(skip + idx) % len_list = (2 + 0) % 9 = 2 % 9 = 2`
Cogemos el elemento de índice 2

- 2ª Iteración:
Básicamente 2 + 2 = 4, debido a que el operador módulo (`%`) siempre devuelve el primero operando si este es menor que el segundo (esta vez 8).
Como ahora el array contiene los elementos: `['1', '2', '4', '5', '6', '7', '8', '9']`, el índice 4 no será el número 5, sino el 6.

Cuando la variable `idx` supere al número de elementos del array, se iniciará por el principio gracias a `%`.

___________________________________



>Fuente: 
https://github.com/keon/algorithms/blob/master/array/circular_counter.py


