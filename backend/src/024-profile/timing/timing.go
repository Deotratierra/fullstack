package main

import (
    "time"
    "log"
)

func Timing(invocation time.Time, name string) {
    elapsed := time.Since(invocation)
    log.Printf("La función %s ha durado %s\n", name, elapsed)
}

func FactorialTimed(x int) int {
    // La palabra clave 'defer' en Golang indica programa la ejecución
    // de una función a justo antes que la función donde se encuentre devuelva
    // un valor. Sin embargo, los argumentos son evaluados al llegar el
    // programa a este punto, por ello 'time.Now()' (el tiempo de comienzo
    // del cronómetro) se evaluará antes de empezar la función.
    defer Timing(time.Now(), "FactorialTimed")

    res := 1
    for i := 1; i <= x; i++ {
        res = res * i
    }

    return res
}

func main() {
    resultado := FactorialTimed(5)
    log.Printf("Resultado = %d\n", resultado)
}

/* Fuentes:
https://tour.golang.org/flowcontrol/12
https://github.com/tmrts/go-patterns/blob/master/profiling/timing.md
*/
