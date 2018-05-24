package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    // Creamos direcciones IP versiones 4 y 6
    IPv4AddrString := "127.0.0.1"
    IPv6AddrString := "2001:db8::68"

    // Parseamos cada versión en un objeto
    // type IP []byte con la función 'net.ParseIP()'
    // https://golang.org/pkg/net/#ParseIP

    IPv4Addr := net.ParseIP(IPv4AddrString)
    if addr == nil {
        fmt.Printf("Invalid address.\n")
    } else {
        fmt.Printf("IPv4 address: '%s'\n", IPv4Addr.String())
    }

    IPv6Addr := net.ParseIP(IPv6AddrString)
    if addr == nil {
        fmt.Printf("Invalid address.\n")
    } else {
        fmt.Printf("IPv6 address: '%s'\n", IPv6Addr.String())
    }

}