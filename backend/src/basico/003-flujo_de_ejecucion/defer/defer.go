package main

/* Lo que realiza una sentencia 'defer' es
    apilar las llamadas en una pila que
    es ejecutada cuando la función actual vuelve.
*/

import (
    "fmt"
)

func main() {
    for i := 0; i <= 10; i++ {
        // Usando defer cada llamada se va apilando
        //  en una pila LIFO, por lo que este bucle
        //  aparece en orden inverso en la salida.
        defer fmt.Printf("%d\n", i)
    }
}
