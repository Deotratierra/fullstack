package main

import (
    "fmt"
    "math"
)

/**
 * Convierte un número entero en formato decimal
 *    en su equivalente binario
 * @param  num Número decimal entero a convertir
 * @return     Devuelve el número pasado como
 *                 argumento en formato binario
 */
func decimalToBinary(num int) int {
    response, resto, pos := 0, 0, 1
    // paso = 1;   // Descomenta para ver el proceso

    for {
        resto = num % 2
        // Descomenta la siguiente línea para ver el proceso:
        //printf("Paso %d: %d/2, Resto = %d, Cociente = %d\n", paso++, num, resto, num/2);
        num /= 2
        response += resto * pos
        pos *= 10
        if num == 0 {
            break
        }
    }
    return response;
}

/**
 * Convierte un número en formato binario en su equivalente
 *     en decimal como entero.
 * @param  num Número binario a convertir en decimal.
 * @return   Devuelve el número binario pasado como argumento
 *               en su formato decimal.
 */
func binaryToDecimal(num int) int {
    response, exp, resto := 0, 0, 0
    for {
        resto = num % 10
        num /= 10
        response += resto*int(math.Pow(2.0, float64(exp)))
        exp++
        if num == 0 {
            break
        }
    }
    return response
}

func main() {
    var numero int = 56

    binario := decimalToBinary(numero)
    fmt.Printf("El número %d en binario es %v\n",
               numero, binario)     // 10

    decimal := binaryToDecimal(numero)
    fmt.Printf("El número %d en decimal es %v\n",
               numero, decimal)  // 8
}
