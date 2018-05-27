package main

/* Golang no es un lenguaje orientado a objetos, por lo tanto
    no es posible crear clases al uso. En su lugar, Golang
    permite la creación de interfaces, las cuales pueden
    almacenar métodos para una implementación concreta.
*/

import (
    "fmt"
)

type Geometria interface {
    area()  float64
}

type Rectangulo struct {
    base, altura float64
}

type Trapecio struct {
    base_mayor, base_menor, altura float64
}

// Método para calcular el área de los rectángulos
//   implementando la interfaz
func (geom Rectangulo) area() float64 {
    return geom.base * geom.altura
}

// Método para calcular el área de los trapecios
//   implementando la interfaz
func (geom Trapecio) area() float64 {
    return (geom.base_mayor + geom.base_menor) * geom.altura / 2
}

// Método común a todas las geometrías
func getArea(geom Geometria) float64 {
    return geom.area()
}

// ================================================================

func main() {
    rectangulo := Rectangulo{base: 4, altura: 3}
    trapecio := Trapecio{base_mayor: 5, base_menor: 3, altura: 2}

    fmt.Printf("El área del rectángulo es: %v\n", rectangulo.area())
    fmt.Printf("El área del trapecio es: %v\n", getArea(trapecio))
}

/* Fuentes:
https://codingornot.com/15-go-to-go-interfaces-y-metodos
*/
