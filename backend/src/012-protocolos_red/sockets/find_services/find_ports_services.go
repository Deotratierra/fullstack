package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    networkType := "tcp"   // "tcp" o "udp"
    service := "telnet"    // "telnet", "domain", "ssh", "smtp"...

    port, err := net.LookupPort(networkType, service)
    if err != nil {
        fmt.Printf("Error obteniendo el puerto para el " +
                   "servicio '%s' sobre el tipo de red '%s'.\n",
                   service, networkType)
        os.Exit(1)
    } else {
        fmt.Printf("Puerto del servicio '%s': %d\n", service, port)
    }
}