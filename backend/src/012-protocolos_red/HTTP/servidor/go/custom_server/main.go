package main

import (
    "fmt"
    "net/http"
    "log"
    "io/ioutil"
)

func main() {
    // Lanzamos una petición al servidor
    resp, err := http.Get("http://localhost:8765/hello")

    if (err != nil){  // manejamos el posible error
        log.Fatal(err)
    } else {
        // La petición es correcta, imprimimos el objeto response
        fmt.Printf("REQUEST OK!\n")
        fmt.Println("Response:", resp)

        // Registramos el cierre del cuerpo de la petición
        defer resp.Body.Close()
        // Leemos el cuerpo (lo obtenemos como arreglo de bytes)
        body, err := ioutil.ReadAll(resp.Body)
        if (err != nil){
            log.Fatal(err)
        }

        // Imprimimos la respuesta haciendo un casting a cadena
        fmt.Printf("%s", string(body)) // ¡Hola mundo desde un servidor personalizado!
    }
}
