package main

import (
    "net/http"
    "time"
    "log"
    "fmt"
    "io"
)

func HelloServer(w http.ResponseWriter, req *http.Request) {
	fmt.Printf("Ha llegado una petición desde la IP '%s'.\n", req.RemoteAddr)

    // Enviamos la respuesta
    io.WriteString(w, "¡Hola mundo desde un servidor personalizado!\n")
}


func main() {
    server := &http.Server{
        Addr:           ":8765",
        ReadTimeout:    10 * time.Second,
        WriteTimeout:   10 * time.Second,
        MaxHeaderBytes: 1 << 20,
    }

    http.HandleFunc("/hello", HelloServer)

    log.Fatal(server.ListenAndServe())
}
