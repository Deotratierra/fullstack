
package main

//import "math"

func mayor(a int, b int) (int) {
    if a >= b {
        return a
    } else {
        return b
    }
}

func main() {
    num1, num2 := 3, 5  // Asignación múltiple
    println(mayor(num1, num2))

    // También así (requiere descomentar import "math":
    //respuesta := int( math.Max(float64(num1), float64(num2)) )
    //println(respuesta)
}

/* Fuentes:
https://golang.org/pkg/math/#Max
https://stackoverflow.com/questions/19230191/convert-an-integer-to-a-float-number-in-golang
*/
