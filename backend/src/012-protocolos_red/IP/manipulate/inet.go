package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    // =============================================

    //         Parsear cadenas IP
    
    /* Podemos crear objetos del tipo 'net.IP' de varias formas.
    En este primer ejemplo parseamos direcciones IP
    con la función 'net.ParseIP()'.
    */

    // Creamos direcciones IP versiones 4 y 6
    IPv4AddrString := "127.0.0.1"
    IPv6AddrString := "2001:db8::68"

    // Parseamos cada versión en un objeto
    // type IP []byte con la función 'net.ParseIP()'
    // https://golang.org/pkg/net/#ParseIP

    IPv4Addr := net.ParseIP(IPv4AddrString)
    if IPv4Addr == nil {
        fmt.Printf("Dirección inválida.\n")
    } else {
        fmt.Printf("Dirección IPv4: '%s'\n", IPv4Addr.String())
        fmt.Printf("Tipo del objeto IP: %T\n", IPv4Addr)
    }

    IPv6Addr := net.ParseIP(IPv6AddrString)
    if IPv6Addr == nil {
        fmt.Printf("Dirección inválida.\n")
    } else {
        fmt.Printf("Dirección IPv6: '%s'\n", IPv6Addr.String())
        fmt.Printf("Tipo del objeto IP: %T\n", IPv6Addr)
    }

    fmt.Printf("\n")

    /* En este segundo ejemplo creamos direcciones IPv4
    por medio de la estructura 'net.IPv4'.
    */

    fmt.Printf("%[1]s - %[1]T\n", net.IPv4(8, 8, 8, 8))

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
