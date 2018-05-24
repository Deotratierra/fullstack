package main

import (
   "fmt"
   "runtime"
   "strconv"
   "math"
)

/* Tipos de enteros independientes de la arquitectura:

uint8   ->  el conjunto de todos los enteros sin signo de  8-bit (0 a 255)
uint16  ->  el conjunto de todos los enteros sin signo de 16-bit (0 a 65535)
uint32  ->  el conjunto de todos los enteros sin signo de 32-bit (0 a 4294967295)
uint64  ->  el conjunto de todos los enteros sin signo de 64-bit (0 a 18446744073709551615)

int8    ->  el conjunto de todos los enteros con signo de  8-bit (-128 a 127)
int16   ->  el conjunto de todos los enteros con signo de 16-bit (-32768 a 32767)
int32   ->  el conjunto de todos los enteros con signo de 32-bit (-2147483648 a 2147483647)
int64   ->  el conjunto de todos los enteros con signo de 64-bit (-9223372036854775808 a 9223372036854775807)


   Tipos de enteros dependientes de la arquitectura:

uint    ->  32 ó 64 bits
int     ->  mismo tamaño que 'uint'
uintptr ->  un entero sin signo tan largo como para almacenar los bits no interpretados del valor de un puntero

*/

func main(){
    fmt.Printf("Sistema operativo: %s - Arquitectura %s\n",
    	       runtime.GOOS, runtime.GOARCH)

    // Obtener el tamaño de 'int':
    fmt.Printf("Tamaño de 'int': %d bits (%v bytes).\n",
    	        strconv.IntSize, math.Sqrt(strconv.IntSize))

    // Obtener el tamaño de 'uintptr'
    const UintPtrSize = 32 << uintptr(^uintptr(0)>>63)
    fmt.Printf("Tamaño de 'uintptr': %d bits (%v bytes).\n",
    	       UintPtrSize, math.Sqrt(UintPtrSize))
}
