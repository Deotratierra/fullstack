// Go soporta punteros, los cuales nos permiten pasar referencias
// de valores y datos entre las funciones de nuestro programa.

// A diferencia de C, Golang no soporta aritmética de punteros.

package main

import "fmt"

// Veamos como los apuntadores funcionan en contraste con los valores directos
// utilizando dos funciones: `zeroval` y `zeroptr`. `zeroval` recibe
// un parametro `int`, así que los argumentos serán pasados por valor.
// `zeroval` va a recibir una copia de `ival` distinta a la de la función
// donde se llama.
func zeroval(ival int) {
    ival = 0
}

// `zeroptr` recibe un parametro `*int`, lo que significa
// que recibe un apuntador a un valor `int`.
// Si asignamos un valor a un apuntador referenciado se cambia el valor
// que se está almacenando en dicha dirección de memoria.
func zeroptr(iptr *int) {
    *iptr = 0
}

func main() {
    i := 1
    fmt.Println("initial:", i)

    zeroval(i)
    fmt.Println("zeroval:", i)

    // La sintaxis `&i` devuelve la dirección en memoria de `i`,
    // i.e. un apuntador a `i`.
    zeroptr(&i)
    fmt.Println("zeroptr:", i)

    // Los apuntadores también pueden mostrarse en pantalla
    fmt.Println("pointer:", &i)
}

/* Fuentes:
http://www.goconejemplos.com/apuntadores
*/
