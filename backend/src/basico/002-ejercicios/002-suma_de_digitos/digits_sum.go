package main

import "strconv"

var num1 int = 4511
var num2 int = 369301

/* Con la función ``strconv.Itoa()`` convertimos
    los números enteros en cadenas. */

func digits_sum(number int) (string) {
    var response string = ""
    var total int = 0
    for {
        if number == 0 { break }
        rest := number % 10
        response += strconv.Itoa(rest)
        total += rest
        number = int(number/10)
        if number > 0 {
            response += " + " // Las cadenas se pueden
        }                     // concatenar con el operador de suma
    }
    response += " = " + strconv.Itoa(total)
    return response
}

func main() {
    println(digits_sum(num1))
    println(digits_sum(num2))
}

/* Fuentes:
https://stackoverflow.com/questions/10105935/how-to-convert-an-int-value-to-string-in-go/10105983#10105983
*/
