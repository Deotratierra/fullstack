package main

import (
    "fmt"
)

// Creamos un operador abstracto
// por medio de una interface.
type Operador interface {
    Aplicar(int, int) int
}

// Creamos una operación abstracta,
// cuya implementación dependerá del operador.
type Operacion struct {
    Operador Operador
}

// Al llamar al método 'Operar()' de una implementación
// se ejecutará la función 'Aplicar()'.
func (o *Operacion) Operar(x, y int) int {
    return o.Operador.Aplicar(x, y)
}

// ------------------------------

// Creamos un operador concreto, el de suma.
// Este lo pasaremos a una estructura 'Operacion'.
type Suma struct{}

// Creamos la función que se ejecutará
func (Suma) Aplicar(x, y int) int {
    return x+y
}
func main() {
    // Instanciamos una operación
    suma := Operacion{Suma{}}

    x, y := 3, 6

    // Aplicamos la operación a los parámetros
    resultado := suma.Operar(x, y)
    fmt.Printf("%d + %d = %d\n", x, y, resultado)
}

/* Fuentes:
https://github.com/tmrts/go-patterns/blob/master/behavioral/strategy.md
*/
