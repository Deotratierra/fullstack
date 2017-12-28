## Punteros
El valor de cada variable está almacenado en un lugar determinado de la memoria, caracterizado por una dirección (que se suele expresar en hexadecimal). El ordenador mantiene una tabla de direcciones (ver abajo) que relaciona el nombre de cada variable con su dirección en la memoria. Gracias a los nombres de las variables (identificadores), en general no hace falta que el programador se preocupe de la dirección de memoria donde están almacenados sus datos.

| Variable | Dirección de memoria |
|----------|----------------------|
|    A     | 000FA:000            |
|    B     | 000FA:002            |
|    C     | 000FA:004            |
|    p1    | 000FA:006            |
|    p2    | 000FA:00A            |

Así pues, un puntero es una variable que puede contener la dirección de otra variable. Por tanto, los punteros están almacenados en algún lugar de la memoria y tienen su propia dirección.