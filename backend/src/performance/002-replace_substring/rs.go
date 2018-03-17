package main

import "strings"

func main() {
    var _str string = "Salida de emergencia"
    var pattern string = "Salida"
    var substitution string = "Entrada"

    strings.Replace(_str, pattern, substitution, -1)
}
