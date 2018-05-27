package main

import (
    "fmt"
)

func main() {
    // Las cadenas UTF-8 en Golang deben ir entre
    //  caracteres ``, las cuales indican texto literal,
    //  como en NodeJS.
    const utf8_str = `⌘`

    // Imprimir caracteres UTF-8
    fmt.Printf("plain string: %s\n",
               utf8_str)                // ⌘

    // Imprimir la secuencia de escape
    fmt.Printf("quoted string: %+q\n",
               utf8_str)                // "\u2318"

    // Imprimir los bytes de la cadena en hexadecimal
    fmt.Printf("hex bytes: ")
    for i := 0; i < len(utf8_str); i++ {
        fmt.Printf("%x ", utf8_str[i])  // e2 8c 98
    }
    fmt.Printf("\n")
}
