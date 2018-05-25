package main

import (
   "fmt"
   "bytes"
   "log"
)

func main() {
    /* La función 'log.New' crea un nuevo logger
        Toma un buffer de bytes como primer parámetro,
        un prefijo a todos los mensajes como segundo
        y las propiedades del logger como tercero.
        https://golang.org/pkg/log/#New
    */
    var (
		buf    bytes.Buffer
		logger = log.New(&buf, "logger: ", log.Lshortfile)
	)

    // Escribimos en el buffer
    logger.Print("¡Hola buffer del logger!")
    logger.Printf("%s\n", "Te escribo otro mensaje.")

    // Imprimimos todos los mensajes almacenados en el buffer
    fmt.Print(&buf)
}
