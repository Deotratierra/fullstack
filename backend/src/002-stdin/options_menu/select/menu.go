package main

import (
    "fmt"
    "bytes"

    "github.com/pkg/term"
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
    options := [4]string{"Opción 1", "Opción 2", "Opción 3", "Salir"}
    for i, opt := range options {
        fmt.Printf("%d) %s\n", i+1, opt)
    }
    fmt.Printf("Elige una opción: ")
    for {
        c := getch()
        fmt.Printf("\n")
        switch {
        case bytes.Equal(c, []byte{49}):  // tecla 1
            fmt.Printf("Has elegido la %s.\n", options[0])
            return
        case bytes.Equal(c, []byte{50}):  // tecla 2
            fmt.Printf("Has elegido la %s.\n", options[1])
            return
        case bytes.Equal(c, []byte{51}):  // tecla 3
            fmt.Printf("Has elegido la %s.\n", options[2])
            return
        case bytes.Equal(c, []byte{52}):  // tecla 4
            fmt.Printf("¡Hasta luego!\n")
            return
        default:
            fmt.Printf("Opción inválida. Caracter: %c | Ascii: %d\n", c, c)
        }
        return
    }
}
