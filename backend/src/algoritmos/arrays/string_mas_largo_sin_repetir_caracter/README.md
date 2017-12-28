### Problema
Dada una cadena de caracteres, buscar la longitud de la subcadena más larga sin repetir caracteres.

Ejemplos:
- `"abcabcbb`, la respuesta es `"abc"`, cuyo largo es 3.
- `"bbbbb"`, la respuesta es `"b"`, cuyo largo es 1.
- `"pwwkew"`, la respuesta es `"wke"`, cuyo largo es 3.

________________________________

### Explicación

El punto está en jugar cion 3 variables, una para indicar el índice de comienzo de la subcadena, otra para indicar el largo máximo encontrado y otra como hash para guardar los caracteres usados. 
Por cada caracter comprobamos si lo hemos usado antes, antes del principio para ahorrar la entrada al bucle, y, si es así, indicamos que ahí comienza la subcadena.
Si no, comprobamos cuántas posiciones de diferencia hay entre el caracter actual y el principio de la subcadena, y, si es mayor que el indicador de la subcadena más larga, lo actualizamos al nuevo récord de longitud.


> Fuente: https://github.com/keon/algorithms/blob/master/array/longest_non_repeat.py