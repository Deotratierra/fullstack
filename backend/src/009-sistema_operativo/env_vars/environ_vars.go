package main

import (
   "fmt"
   "os"
   "strings"
)

func main() {
    // Establecer una variable de entorno
    os.Setenv("FOO", "hola")

    // Obtener el valor de variables de entorno
    fmt.Printf("FOO = '%s'\n", os.Getenv("FOO"))  // FOO = 'hola'
    fmt.Printf("BAR = '%s'\n\n", os.Getenv("BAR"))  // BAR = ''

    // Acceso a todas las variables de entorno
    for _, variable := range os.Environ() {
        pair := strings.Split(variable, "=")
        fmt.Printf("%s = %s\n", pair[0], pair[1])
    }
}
