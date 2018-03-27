package main

import (
    "crypto/md5"
    "fmt"
)

func main() {
    // Crear un hash MD5
    h := md5.New()
    fmt.Printf("%x\n", h.Sum(nil))
    //             d41d8cd98f00b204e9800998ecf8427e

    // -----------------------------------------

    // Crear un hash MD5 a partir de ciertos datos
    data := []byte("Algunos datos para hashear")
    fmt.Printf("%x\n", md5.Sum(data))
    //             40bc8d3969bbb3037dc6b0f9be372409

}

/* Fuentes:
https://golang.org/pkg/crypto/md5/#example_New_file
*/
