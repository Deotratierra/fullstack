package main

import (
    "fmt"
    "os"
)

func main() {
    path := "ejemplo.txt"

    // Intentamos abrir el archivo
    f, err := os.OpenFile(path, os.O_RDWR, os.ModeAppend)
    if err != nil {  // si salta un error
        f, err = os.Create(path)  // intentamos crearlo
        if err != nil {
            fmt.Printf("Error creando el archivo '%s':\n", path)
            fmt.Printf("%s\n", err.Error())
        } else {
            f, err = os.OpenFile(path, os.O_RDWR, os.ModeAppend)
        }
    }

    // Escribir en archivos
    n, err := f.WriteString("Contenido del archivo\n")
    if err != nil {
        fmt.Printf("Error escribiendo en el archivo '%s':\n", path)
        fmt.Printf("%s\n", err.Error())
    } else {
        fmt.Printf("%d bytes escritos en el archivo correctamente\n", n)
    }
    fmt.Printf("\n")

    // Leer desde archivos
    _, err = f.Seek(0, 0)  // Reiniciamos la posición del buffer al archivo
    if err != nil {
        fmt.Printf("Error reiniciando el archivo '%s' a su posición inicial:\n", path)
        fmt.Printf("%s", err.Error())
    }
    b := make([]byte, n)  // Creamos un buffer de bytes
    _, err = f.Read(b)    // Leemos el contenido en el buffer
    if err == nil {
        s := string(b[:n])    // Convertimos el buffer a cadena
        fmt.Printf("El archivo fue leído correctamente:\n%s", s)
    } else {
        fmt.Printf("Ocurrió un error leyendo el archivo '%s':\n", path)
        fmt.Printf("%s", err.Error())
    }
}

/* Fuentes:
https://stackoverflow.com/questions/12518876/how-to-check-if-a-file-exists-in-go
https://medium.com/golangspec/scopes-in-go-a6042bb4298c
https://stackoverflow.com/questions/33851692/golang-bad-file-descriptor/33852107
*/