package main

import (
    "fmt"
    "reflect"
)

/* Para obtener el tipo de una variable en Golang
    podemos utilizar la función 'reflect.TypeOf()'
    o el formateo de cadenas '%T'.
*/

func main(){
    TrueFalse := false

    // Usando formateo de cadenas:
    fmt.Printf("%T\n", TrueFalse)     // bool

    // Usando el paquete 'reflect':
    fmt.Printf("%s\n", reflect.TypeOf(TrueFalse))   // bool
}
