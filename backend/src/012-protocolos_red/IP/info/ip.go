package main

import (
   "fmt"
   "os"
   "log"
   "net"
)

// Obtener la IP local
// https://stackoverflow.com/questions/23558425/how-do-i-get-the-local-ip-address-in-go
func GetOutboundIP() net.IP {
    conn, err := net.Dial("udp", "8.8.8.8:80")
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    localAddr := conn.LocalAddr().(*net.UDPAddr)

    return localAddr.IP
}

func main() {
    // Obtener el nombre del host local
    hostname, err := os.Hostname()
    // https://golang.org/pkg/os/#Hostname

    if (err != nil){
        log.Fatal(err)
    } else {
        fmt.Printf("%s\n", hostname)
    }

    // Obtener la IP local
    localAddr := GetOutboundIP()
    fmt.Printf("%s\n", localAddr)
}

/* Fuentes:
https://stackoverflow.com/questions/23558425/how-do-i-get-the-local-ip-address-in-go
*/