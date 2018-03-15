package main

import (
    "bufio"     // https://golang.org/pkg/bufio/
    "fmt"
    "os"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Escribe tu nombre: ")
    name, _ := reader.ReadString('\n')
    fmt.Printf("Bienvenid@ a mi documentación, %s.\n",
    	       name[0:len(name)-1])  //  Se elimina el último
}              // caracter ya que corresponde a un salto de
               // línea (ENTER)
