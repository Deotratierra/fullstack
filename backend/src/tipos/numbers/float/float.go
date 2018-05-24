package main

import (
    "fmt"
    "math"
    "encoding/binary"
)

/* En Golang existen dos tipos para representar
    números de punto flotante: 'float32' y 'float64'.
    Su tamaño en bits lo indica el número en el nombre
    del tipo. El tipo 'float64' tiene más precisión
    que el tipo 'float32'.
*/

func main(){

    // Obtener el número máximo y mínimo de cada tipo
    //     float32
    fmt.Printf("float32 - Máximo: %v\n", math.MaxFloat32)
    fmt.Printf("float32 - Mínimo: %v\n", math.SmallestNonzeroFloat32)

    //     float64
    fmt.Printf("float64 - Máximo: %v\n", math.MaxFloat64)
    fmt.Printf("float64 - Mínimo: %v\n\n", math.SmallestNonzeroFloat64)


    // Calcular el tamaño en bytes
    var flotante_32_bits float32
    flotante_32_bits = 1.1234
    fmt.Printf("float32 - Bytes: %d\n", binary.Size(flotante_32_bits))  // 4

    var flotante_64_bits float64
    flotante_64_bits = 1.1234
    fmt.Printf("float64 - Bytes: %d\n\n", binary.Size(flotante_64_bits))  // 8


    // ===============================================================

    // Formatear números de punto flotante
    fmt.Printf("Número flotante: %v\n", flotante_32_bits)
}