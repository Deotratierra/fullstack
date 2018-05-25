package main

import (
    "fmt"
    "time"
    "math/rand"
)

// Comunicación entre goroutines mediante canales

func aburrido(msg string, c chan string) {
    for i := 0; ; i++ {
        c <- fmt.Sprintf("%s %d", msg, i)
        time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
    }
}

func main() {
    // Creamos un canal
    c := make(chan string)
    go aburrido("¡Aburrido!", c)

    // Recibimos el mensaje desde la goroutine
    //   a través del canal
    for i := 0; i < 5; i++ {
        fmt.Printf("Mensaje recibido de " +   // La llegada del mensaje bloquea
        	       "la goroutine: %q\n", <-c) // la ejecución mientras no llega
    }
    fmt.Println("Que aburrimiento... me piro.")
}
