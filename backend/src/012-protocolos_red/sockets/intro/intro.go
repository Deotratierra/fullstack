package main

import (
    "fmt"
    "net"
    "os"
    "io/ioutil"
)

func main() {
    addr := "www.google.com:80"

    // Convertimos la dirección en una estructura 'net.TCPAddr'
    // https://golang.org/pkg/net/#TCPAddr
    tcpAddr, err := net.ResolveTCPAddr("tcp4", addr)
    if err != nil {
        fmt.Printf("Error resolviendo la dirección TCP para '%s': %s\n",
                   addr, err.Error())
        os.Exit(1)
    }

    /* La función 'net.DialTCP()' crea una conexión con una
    dirección remota usando el protocolo TCP.
    https://golang.org/pkg/net/#Dial
    https://golang.org/pkg/net/#DialTCP
    */
    conn, err := net.DialTCP("tcp", nil, tcpAddr)
    if err != nil {
        fmt.Printf("Error estableciendo una conexión TCP con '%s': %s\n",
                   tcpAddr, err.Error())
        os.Exit(1)
    } else {
        fmt.Printf("Conexión TCP ")
    }

    /* Las peticiones HEAD piden a un servidor información
    sobre el mismo y un documento del servidor. El servidor
    devuelve información, pero no el documento en sí mismo.
    La petición de este ejemplo pide información sobre el
    documento raíz del servidor: */
    _, err = conn.Write([]byte("HEAD / HTTP/1.0\r\n\r\n"))
    if err != nil {
        fmt.Printf("Error escribiendo en el socket: %s\n", err.Error())
        os.Exit(1)
    }

    /* Leemos la respuesta con la función 'ioutil.ReadAll()'.
    Esta función espera que el servidor termine de enviar
    información para devolver el mensaje completo. */
    result, err := ioutil.ReadAll(conn)
    if err != nil {
        fmt.Printf("Ocurrió un error leyendo la respuesta del servidor: %s\n",
                   err.Error())
        os.Exit(1)
    } else {
        fmt.Printf("La respuesta del servidor es:\n\n%s", string(result))
        os.Exit(0)
    }

}
