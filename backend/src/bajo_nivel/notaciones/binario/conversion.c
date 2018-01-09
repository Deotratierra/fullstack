#include <stdio.h>
#include <math.h>

/* Compilación linkeando con el cabecero <math.h>
    gcc conversion.c -o conversion -lm
*/

// =================================================

/**
 * Convierte un número entero en formato decimal
 *    en su equivalente binario
 * @param  num Número decimal entero a convertir
 * @return     Devuelve el número pasado como
 *                 argumento en formato binario
 */
long long decimalToBinary(int num) {
    long long response = 0;
    int resto, pos = 1;
    // paso = 1;   // Decomenta para ver el proceso

    while (num!=0)
    {
        resto = num % 2;
        // Descomenta la siguiente línea para ver el proceso:
        //printf("Paso %d: %d/2, Resto = %d, Cociente = %d\n", paso++, num, resto, num/2);
        num /= 2;
        response += resto * pos;
        pos *= 10;
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
int binaryToDecimal(long long num) {
    int response = 0, exp = 0, resto;
    while (num!=0)
    {
        resto = num % 10;
        num /= 10;
        response += resto*pow(2,exp);
        ++exp;
    }
    return response;
}

// =============================================================

int main() {
    int numero = 56, binario, decimal;

    // Conversión de decimal a binario
    binario = decimalToBinary(numero);
    printf("El número %d en binario es %d\n", numero, binario);

    // Conversión de binario a decimal
    decimal = binaryToDecimal(binario);
    printf("El número %d en decimal es %d\n", binario, decimal);

    return 0;
}