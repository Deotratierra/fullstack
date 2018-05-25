package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    // =============================================

    //         Parsear cadenas IP

    // Creamos direcciones IP versiones 4 y 6
    IPv4AddrString := "127.0.0.1"
    IPv6AddrString := "2001:db8::68"

    // Parseamos cada versión en un objeto
    // type IP []byte con la función 'net.ParseIP()'
    // https://golang.org/pkg/net/#ParseIP

    IPv4Addr := net.ParseIP(IPv4AddrString)
    if IPv4Addr == nil {
        fmt.Printf("Invalid address.\n")
    } else {
        fmt.Printf("IPv4 address: '%s'\n", IPv4Addr.String())
    }

    IPv6Addr := net.ParseIP(IPv6AddrString)
    if IPv6Addr == nil {
        fmt.Printf("Invalid address.\n")
    } else {
        fmt.Printf("IPv6 address: '%s'\n", IPv6Addr.String())
    }


    fmt.Printf("\n")
    // ===============================================

    //         Obtener IP de un host remoto

    hostname := "www.google.com"

    addr, err := net.ResolveIPAddr("ip", hostname)
    if err != nil {
        fmt.Printf("Error resolviendo el hostname '%s': %s\n", hostname, err.Error())
        os.Exit(1)
    } else {
        fmt.Printf("La dirección IP del host '%s' es '%s'.\n", hostname, addr.String())
    }

    // ===============================================
}

/* Fuentes:
http://tumregels.github.io/Network-Programming-with-Go/socket/ip_address_type.html
*/
