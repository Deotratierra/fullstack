package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Printf("Sistema operativo: %s\n", runtime.GOOS)
}
