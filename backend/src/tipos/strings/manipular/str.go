package main

import (
    "fmt"
    "strings"
    "strconv"   // https://golang.org/pkg/strconv/
)

/*            Cadenas de caracteres en Golang
En la mayoría de lenguajes de programación, las cadenas suelen
    ser un arreglo de caracteres, pero en Go son una secuencia
    de bytes, pues en este lenguaje no existe el tipo 'char'.

Las cadenas son inmutables, lo cual significa que al definir
    un nuevo valor en una variable de tipo string, se crea
    una nueva variable en memoria.
*/

func main() {
    // Inicialización
    var cadena string  // Cadena en una sóla línea:
    cadena = "HOLA"
    fmt.Printf("%s\n", cadena)     // ¡En Go no se declaran cadenas
                                   //     con comillas simples!
    // Cadena en varias líneas:
    html := `<html>
  <head>
  </head>
  <body>
    <h1>Hola mundo</h1>
  </body>
</html>`
    fmt.Printf("%s\n", html)

    // Escape de caracteres especiales
    cadena_escape := "Hola \"Mundo\""
    fmt.Printf("%s\n", cadena_escape)   // Hola "Mundo"


    // Saber el tamaño de una cadena
    fmt.Printf("El tamaño de '%s' es %d.\n",
    	       cadena, len(cadena))

    // Acceso a los elementos mediante índices
    fmt.Printf("Primer caracter: '%c'.\n", cadena[0])   // H
    /* Si accedemos a los elementos de la cadena formateándolos
        como cadenas ("%s") nos devolvera el número correspondiente
        del caracter con el estándar ASCII. Para obtener el caracter
        lo formateamos con "%c".

       Los índices negativos no están permitidos en Go. Por lo tanto,
       si queremos acceder a los últimos 3 caracteres de una cadena
       debemos realizar lo siguiente:
    */
    fmt.Printf("Últimos tres caracteres de la cadena: '%s'.\n",
               cadena[:len(cadena)-3])
    // o también
    //fmt.Printf("Últimos tres caracteres de la cadena: '%s'.\n",
    //           cadena[len(cadena)-3:len(cadena)])

    // Acceso a un trozo de la cadena
    fmt.Printf("%s\n", cadena[1:4])  // OLA

    /* Debido a que las cadenas son inmutables, el siguiente código
        (descomentado) produce errores:
    */
    //cadena[2] = "W"

    // =============================================================
    //                   Operaciones con cadenas

    // Concatenar cadenas     (creando una nueva cadena en memoria)
    nueva_cadena := cadena + " MUNDO"
    fmt.Printf("%s\n", nueva_cadena)  // HOLA MUNDO
    // También así:
    nueva_cadena += " FELIZ"
    fmt.Printf("%s\n", nueva_cadena)  // HOLA MUNDO FELIZ

    // Reemplazar subcadenas
    cadena = strings.Replace(cadena, "OLA", "ALO", -1)
    fmt.Printf("%s\n", cadena)        // HALO

    // Iterar por los caracteres de una cadena
    for pos, char := range "日本語" {
	    fmt.Printf("El caracter %c empieza en la posición %d.\n",
	    	       char, pos)
	}

    // ------------------------------------------------------------

    //                  Conversiones
    // De entero a string
    fmt.Printf("Hola " + strconv.Itoa(55) + "\n")  // Hola 55

    // De string a entero
    i1, _ := strconv.Atoi("5")
    fmt.Printf("%d\n", 5 + i1)  // 10

    i2, _ := strconv.ParseInt("5", 10, 64) // También así
    fmt.Printf("%d\n", 5 + i2)  // 10

    // De float a string
    i3 := strconv.FormatFloat(3.33, 'f', 6, 64)
    fmt.Printf("%s\n", i3)  // 3.330000

    // De string a float
    i4, _ := strconv.ParseFloat("3.33", 64)
    fmt.Printf("%f\n", 3.33 + i4)   // 6.660000
}
