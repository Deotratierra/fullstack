package main

import (
   "fmt"
   "strconv"   // https://golang.org/pkg/strconv/
)

/* Las conversiones básicas de tipos en Golang se realizan
    mediante la sintaxis 'T(x)' donde 'T' es el tipo a
    convertir y 'x' es el valor.
*/

func main(){
    //              CONVERSIONES BÁSICAS

    var i int = 42
    fmt.Printf("%[1]T - %[1]d\n", i)    // int - 42

    var f float64 = float64(i)
    fmt.Printf("%[1]T - %[1]v\n", f)    // float64 - 42

    var u uint = uint(f)
    fmt.Printf("%[1]T - %[1]d\n", u)  // uint - 42


    /* Sin embargo otras conversiones de tipos
        como de cadenas a enteros no están permitidas.
        El siguiente código lanza un error en tiempo
        de compilación con el mensaje:
        'cannot convert "56" (type untyped string) to type uint'
    */
    //var hola uint = uint("56")


    // =====================================================

    //              CONVERSIONES COMPLEJAS
    // -----------------------------------------------------

    /* Para cazar las posibles excepciones en las funciones
        del paquete strconv se suele usar algo como:

    if s, err := strconv.ParseBool(v); err == nil {
		fmt.Printf("%T, %v\n", s, s)
	}
    */

    // -----------------------------------------------------

    // De cadenas a enteros
    // https://golang.org/src/strconv/atoi.go
    fmt.Printf("\nDe cadenas a enteros:\n")

    var cadena1 string = "56"
    entero1_desde_cadena1, _ := strconv.Atoi(cadena1)
    fmt.Printf("%[1]T - %[1]d\n", entero1_desde_cadena1)  // int - 56
    //     También:
    entero2_desde_cadena1, _ := strconv.ParseInt(cadena1, 10, 64)
    fmt.Printf("%[1]T - %[1]d\n", entero2_desde_cadena1)  // int64 - 56
    //     Los argumentos 2º y 3º de la función 'ParseInt'
    //       son la base y el número de bits del valor
    //       resultante.

    // ---------------------------------------------------

    // De cadenas a floats
    // https://golang.org/src/strconv/atof.go
    fmt.Printf("\nDe cadenas a floats:\n")

    var cadena2 string = "56.7"

    //     El segundo parámetro de la función 'ParseFloat'
    //       es el número de bits del número producido.
    //       Si pasamos el valor 32, el número producido
    //       no será exacto (al menos en mi ordenador de 64 bits).
    float1_desde_cadena2, _ := strconv.ParseFloat(cadena2, 32)
    fmt.Printf("%[1]T - %[1]v\n", float1_desde_cadena2)  // float64 - 56.70000076293945

    float2_desde_cadena2, _ := strconv.ParseFloat(cadena2, 64)
    fmt.Printf("%[1]T - %[1]v\n", float2_desde_cadena2)  // float64 - 56.7

    // ---------------------------------------------------

    // De cadenas a booleanos
    // https://golang.org/src/strconv/atob.go?s=351:391#L1
    fmt.Printf("\nDe cadenas a booleanos:\n")

    var cadena3 = "false"

    bool1_desde_cadena3, _ := strconv.ParseBool(cadena3)
    fmt.Printf("%[1]T - %[1]v\n", bool1_desde_cadena3)  // bool - false
    //     La función 'ParseBool' acepta las siguientes cadenas:
    //       1, t, T, TRUE, true, True, 0, f, F, FALSE

    // -----------------------------------------------------

    // De enteros a cadenas
    // https://golang.org/src/strconv/itoa.go
    fmt.Printf("\nDe enteros a cadenas:\n")

    var entero1 = 34

    cadena1_desde_entero1 := strconv.Itoa(entero1)
    fmt.Printf("%[1]T - %[1]s\n", cadena1_desde_entero1)  // string - 34

    // -----------------------------------------------------

    // De floats a cadenas
    // https://golang.org/src/strconv/ftoa.go?s=1490:1553#L34
    fmt.Printf("\nDe floats a cadenas:\n")

    var float1 float32 = 3.1415926535

    cadena1_desde_float1 := strconv.FormatFloat(float64(float1), 'f', -1, 32)
    fmt.Printf("%[1]T - %[1]s\n", cadena1_desde_float1)  // string - 3.1415927

    var float2 float64 = 3.1415926535

    cadena1_desde_float2 := strconv.FormatFloat(float2, 'f', -1, 64)
    fmt.Printf("%[1]T - %[1]s\n", cadena1_desde_float2)  // string - 3.1415926535

    // -----------------------------------------------------

    // De booleanos a cadenas
    // https://golang.org/pkg/strconv/#FormatFloat
    fmt.Printf("\nDe booleanos a cadenas:\n")

    var booleano1 = true

    cadena1_desde_booleano1 := strconv.FormatBool(booleano1)
    fmt.Printf("%[1]T - %[1]s\n", cadena1_desde_booleano1)  // string - true

}
