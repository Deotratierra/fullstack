package main

// Golang soporta funciones anónimas que
// pueden ser definidas, instanciadas e
// invocadas de diferentes formas.

import (
    "fmt"
)

// Para aceptar una función como argumento
//   debemos declararla como tipo, cuyo
//   nombre declararemos como tipo del argumento.
type convert func(int) string

// Pasar una función en línea
//   como argumento a una función.
func quote(fn convert) string {
	return fmt.Sprintf("%q", fn(123))
}

// Debemos tener en cuenta que los tipos
//  de esta función deben coincidir con
//  los declarados en el tipo 'convert'.
func value(x int) string {
	return fmt.Sprintf("%v", x)
}


func main() {

    // Llamar a una función anónima en línea
    resultado := func(a, b int, z float64) bool {
    	return a*b == int(z)         // true
    }(2, 4, 8.01)

    fmt.Printf("%v\n", resultado)

    // Instanciar una función anónima en una variable
    suma := func(x, y int) int { return x + y }
    fmt.Printf("%v\n", suma(5, 10))  // 15

    // Pasar una función a una función como callback
    fmt.Printf("%s\n", quote(value))  // "123"
}

/* Fuentes:
https://golang.org/ref/spec#Function_literals
https://play.golang.org/p/XNMtrDUDS0
https://stackoverflow.com/questions/11766320/does-go-have-lambda-expressions-or-anything-similar
*/
