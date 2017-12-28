El problema trata de escribir una función que coja todos los dígitos de un número y sumarlos, para luego devolver una cadena de caracteres con la operación que ha realizado. Por ejemplo:

##### Input:
    num = 4523
##### Output:
    4 + 5 + 2 + 3 = 14

### Algoritmo:
El algoritmo implementado para el cálculo es el siguiente:

    while num != 0  
        sum += num % 10;
        num /= 10;
    return sum

Aplicado paso a paso (para la primera iteración del ejemplo) es:
- Mientras el número de entrada no sea 0:
    - Dividelo entre 10 y guarda el resto (4523 / 10 -> 4520 / 10 -> resto = 3). Vamos acumulando el sumatorio de los restos.
    - Divide el número entre 10, forzándolo a entero (olvidamos la última cifra).
- Al final de la última iteración el número siempre se convierte en 0.

### Fuente:
https://www.w3resource.com/cpp-exercises/for-loop/cpp-for-loop-exercise-84.php



    
    
