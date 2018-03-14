package main

import (
    "fmt"
    "net/http" // https://golang.org/pkg/net/http/
)

const (
  port = ":8888"
)

func HelloWorld(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "¡Hola servidor!")
}

func main() {
    fmt.Printf("Servidor encendido sirviendo en at http://localhost%v.\n", port)
    http.HandleFunc("/", HelloWorld)
    http.ListenAndServe(port, nil)
}
