package main

import (
    "fmt"
)

/* Golang no provee ninguna forma de realizar
    sobrecarga de operadores, pero podemos realizar
    algo parecido con una función "puntero receptor"
*/

type A struct {
    valor1 int
    valor2 int
}

// Un método de suma de los elementos de la estructura
// pasando como punteros tanto la instancia que
// recibe como el parámetro sumado.
func (a *A) Add(v *A) {
    a.valor1 += v.valor1
    a.valor2 += v.valor2
}

func main() {
    x, y := &A{1, 2}, &A{3, 4}

    x.Add(y)  // Esto sería como x + y, pero no es posible en Golang

    fmt.Println(x)  //  &{4 6}
}

/* Fuentes:
https://stackoverflow.com/questions/33040495/golang-operator-overloading
*/
