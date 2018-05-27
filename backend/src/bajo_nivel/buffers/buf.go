package main

/* Un objeto 'bytes.Buffer' es un buffer de bytes
    de tamaño variable con los métodos 'Read' y 'Write'.
    El valor 0 para 'Buffer' es un buffer vacío listo
    para usar.
*/

import (
    "fmt"
    "os"
    "bytes"
)

func main() {
    // Creamos un buffer vacío
    var b bytes.Buffer    // Un buffer no necesita inicialización

    // Escribir en el buffer
    b.Write([]byte("¡Hola "))
    // https://golang.org/pkg/bytes/#Buffer.Write

    // Cambiar el contenido del buffer
    fmt.Fprintf(&b, "mundo!\n")  // La función 'fmt.Fprintf' escribe
                               //  la salida en el buffer del primer parámetro
                               //  https://golang.org/pkg/fmt/#Fprintf

    // Imprimir el contenido del buffer
    b.WriteTo(os.Stdout)  // ¡Hola mundo!
    // https://golang.org/pkg/bytes/#Buffer.WriteTo

}

/* Fuentes:
https://golang.org/pkg/bytes/#example_Buffer
*/
