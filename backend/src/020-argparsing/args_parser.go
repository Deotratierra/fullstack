package main

import (
    "fmt"
    "flag"
)

/* Para pasar argumentos como "flags" ("banderas" o "indicadores")
     en Golang usamos el módulo flag.
   Las declaraciones de banderas están disponibles para tipos
     enteros, booleanos y cadenas. */

func main(){
    // Declaración de una bandera de tipo cadena
    stringFlag := flag.String("palabra", "valor por defecto", "ayuda")

    // Declaración de una bandera de tipo entero
    intFlag := flag.Int("num", 45, "un entero")

    // Declaración de una bandera de tipo booleano
    boolFlag := flag.Bool("bool", false, "un booleano")

    flag.Parse()

    fmt.Println("stringFlag = ", *stringFlag)
    fmt.Println("intFlag = ", *intFlag)
    fmt.Println("boolFlag = ", *boolFlag)


    // Mostar el resto de argumentos posicionales
    fmt.Println("Cola: ", flag.Args())
}

/*

$ run args_parser.go -palabra=hola argpos

  stringFlag =  hola
  intFlag =  45
  boolFlag =  false
  Cola:  [argpos]

*/
