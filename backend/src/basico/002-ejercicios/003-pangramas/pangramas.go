package main

import "strings"

func pangrama(_str string) (bool) {
    var abecedario_ingles = "abcdefghijklmnopqrstuvwxyz"
    var letras string = ""

    _str = strings.Replace(_str, " ", "", -1)
    for _, ch := range _str {
        var ch string = strings.ToLower(string(ch))
        // Recorremos array las letras que tenemos
        var encontrada = false
        for _, letra := range letras {
		        if string(letra) == ch {
		            encontrada = true
		            break
		        }
		    }
		if encontrada == false {
		    letras += ch
		}
    }
    if len(letras) == len(abecedario_ingles) {
        return true
    }
    return false
}


func main() {
    var sentencias [4]string
    sentencias[0] = "abcdefGHIJKLMNopqrstuvwxyz"
    sentencias[1] = "abcdefGHIJKLwNopqrstuvwxyz"
    sentencias[2] = "Texto de ejemplo"
    sentencias[3] = "The quick brown fox jumps over the lazy dog"

    for _, sentencia := range sentencias {
        println(pangrama(sentencia))
    }
}

/* Fuentes:
https://stackoverflow.com/questions/8190540/how-to-replace-a-single-character-inside-a-string-in-golang
https://stackoverflow.com/questions/39245610/golang-converting-from-rune-to-string
https://stackoverflow.com/questions/15323767/does-golang-have-if-x-in-construct-similar-to-python
https://tour.golang.org/moretypes/15
*/