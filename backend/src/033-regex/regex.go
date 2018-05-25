package main

/* Go utiliza la mismas reglas en las
    cadenas de expresiones regulares
    que otros lenguajes como Perl o Python.
*/

import (
    "fmt"
    "regexp"
)

func main() {
    email := "mondejar1994@gmail.com"

    /* La función 'regexp.Compile' devuelve
        la expresión regular compilada como
        un objeto 'regexp.Regexp' o un error.
        https://golang.org/pkg/regexp/#Compile
    La función 'regexp.MustCompile' funciona
        de la misma forma pero sólo devuelve
        el objeto de expresión regular, invoca
        la función 'panic' si se produce un error.
    */

    // Compilar una expresión regular
    var emailExt = regexp.MustCompile(`.([a-z]+)$`)

    // Comprobar si la expresión coincide
    fmt.Printf("%v\n", emailExt.MatchString(email))  // true

    // Buscar todo el texto coincidente sin agrupar
    fmt.Printf("%s\n", emailExt.FindString(email))  // .com

    // Buscar el texto coincidente con una agrupación
    group := emailExt.FindAllStringSubmatch(email, -1)
    fmt.Printf("%s\n", group[0][1])                 // com

    /* Fíjate que todas las funciones llevan la palabra
        'String' en el nombre. Esto significa que toman
        una cadena de caracteres como argumento. Existen
        funciones análogas con el mismo nombre sin la palabra
        'String', como por ejemplo 'FindAll' a las que se
        les debe pasar una cadena de bytes como parámetro.
    */
}

/* Fuentes:
https://golang.org/pkg/regexp
https://github.com/StefanSchroeder/Golang-Regex-Tutorial/blob/master/01-chapter2.markdown
*/
