package main

/* En otros lenguajes como C, un bloque switch
    ejecuta todas las sentencias que vienen a
    continuación de la seleccionada, pero en Golang
    no se ejecutan las siguientes a la seleccionada.
*/

import (
    "fmt"
    "runtime"
)

func main() {
    switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.", os)
	}
}