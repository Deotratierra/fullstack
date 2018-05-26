package main

import (
   "fmt"
   "math"
)

func main() {
    // Las funciones matemáticas del paquete 'math'
    // sólo aceptan valores de tipo 'float64'.
    num := 50.4

    // Raíz cuadrada
    raiz_cuadrada := math.Sqrt(num)
    fmt.Printf("%v\n", raiz_cuadrada)

    // Próximo entero hacia arriba
    prox_int_up := math.Ceil(num)
    fmt.Printf("%v\n", prox_int_up)

    // Próximo entero hacia abajo
    prox_int_down := math.Floor(num)
    fmt.Printf("%v\n", prox_int_down)

    // Valor absoluto
    abs_value := math.Abs(num)
    fmt.Printf("%v\n", abs_value)

    // Cálculo de factorial
    // https://gist.github.com/esimov/9622710

    // Logaritmo natural
    log := math.Log(num)
    fmt.Printf("%v\n", log)

    // Logaritmo en base 10
    log10 := math.Log10(num)
    fmt.Printf("%v\n", log10)
}

/* Fuentes:
https://golang.org/pkg/math/#Abs
https://gist.github.com/esimov/9622710
*/
