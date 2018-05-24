package main

import (
    "fmt"
)

// Declarar estructura
type Persona struct{
    Nombre string
    Edad   uint8
}

func main(){
    // Inicializar estructura
    p1 := &Persona{"Álvaro", 23}

    fmt.Println(p1)  // &{Álvaro 23}

    // Acceder a los miembros de una estructura
    fmt.Printf("Nombre: %s - Edad: %d\n", p1.Nombre, p1.Edad)
    //    Nombre: Álvaro - Edad: 23

}
