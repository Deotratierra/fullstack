package main

import (
    "fmt"
)

func main() {
    // Caracter (es realmente un número)
    caracter := 'a'
    fmt.Printf("Caracter: '%c'\n", caracter)

    // Convertir de caracter a ASCII
    caracter_en_ascii := int(caracter)
    fmt.Printf("ASCII: %d\n\n", caracter_en_ascii)

    // Caracter
    ascii := 97
    fmt.Printf("ASCII: '%d'\n", ascii)

    // Convertir de ASCII a caracter
    ascii_en_caracter := string(ascii)
    fmt.Printf("Caracter: '%s'\n", ascii_en_caracter)
}
