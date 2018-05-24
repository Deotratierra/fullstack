package main

import (
   "fmt"
   "runtime"
)

func BitsArch() int {
    return 32 << uintptr(^uintptr(0)>>63)
}

func main() {
    // Obtener la arquitectura
    fmt.Printf("%s\n", runtime.GOARCH)  // amd64

    // Obtener la arquitectura en bits
    fmt.Printf("%d\n", BitsArch())      // 64
}
