package main

import (
    "log"
    "fmt"
)

// Creamos un tipo abstractor para almacenar funciones
type Object func(int) int

// Creamos el decorador que toma y devuelve una
// función abstracta
func LogDecorate(fn Object) Object {
	return func(n int) int {
		log.Println("Starting the execution with the integer", n)

		result := fn(n)

		log.Println("Execution is completed with the result", result)

        return result
	}
}

// Función a decorar
func Double(n int) int {
    return n*2
}

func main() {

    // Decoramos la función, obtenemos una función decorada
    f := LogDecorate(Double)

    // Llamamos a la función decorada
    fmt.Println(f(5))
}

/* $ go run decorator.go

2018/05/27 18:38:51 Starting the execution with the integer 5
2018/05/27 18:38:51 Execution is completed with the result 10
10
*/

/* Fuentes:
https://github.com/tmrts/go-patterns/blob/master/structural/decorator.md
*/
