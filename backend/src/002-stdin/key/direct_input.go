package main

import (
    "bytes"
    "fmt"

    "github.com/pkg/term"  // go get github.com/pkg/term
)

func getch() []byte {
    t, _ := term.Open("/dev/tty")
    term.RawMode(t)
    bytes := make([]byte, 3)
    numRead, err := t.Read(bytes)
    t.Restore()
    t.Close()
    if err != nil {
        return nil
    }
    return bytes[0:numRead]
}

func main() {
    fmt.Printf("Pulsa la tecla S (caracter 115) para salir: ")
    for {
        c := getch()
        switch {
        case bytes.Equal(c, []byte{115}):  // tecla S
            fmt.Printf("¡Hasta luego!\n")
            return
        case bytes.Equal(c, []byte{27, 91, 68}): // left
            fmt.Println("Has pulsado la tecla izquierda")
        default:
            fmt.Println("Has pulsado una tecla desconocida", c)
        }
        return
    }
    return
}

/* Fuentes:
https://stackoverflow.com/questions/14094190/golang-function-similar-to-getchar
*/
