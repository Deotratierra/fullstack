#include <stdio.h>
#include <math.h>

/* Compilación linkeada con el cabecero <math.h>:
   gcc conversion.c -o conversion -lm
*/

// ====================================================

/**
 * Función para convertir un entero decimal a octal
 * @param numero Entero a convertir
 */
int decimalToOctal(int numero) {
    int unidades = 1, resto, total = 0;
    while (numero > 0)
    {
        resto = numero % 8;   // Vamos dividiendo el número entre 8
        numero /= 8;          // y nos vamos quedando con el resto
        total += unidades * resto;  // Vamos multiplicando el resto por la posición del digito
        unidades *= 10;       // (unidades, decenas, centenas ...)
    }
    return total;
}

/**
 * Función para convertir un entero octal a Decimal
 * @param numero Entero a convertir
 */
int octalToDecimal(int numero) {
    int digito;
    int exp = 0, total = 0;
    while (numero > 0) {
        digito = numero % 10;  // Vamos obteniendo los dígitos de unidades hacia arriba...
        numero /= 10;             // ...y eliminándolos del número
        total += digito * (int)pow(8,exp);
        exp++;
    }
    return total;
}

// ================================================================

int main() {


    int numero, en_decimal, en_octal;
    printf("Introduce un número octal que quieras convertir en decimal: ");
    scanf("%i", &numero);

    // Conversión de un número entero de octal a decimal
    en_decimal = octalToDecimal(numero);
    printf("Conversión de octal a decimal mediante función: %i\n\n", en_decimal);

    // Conversión de un número entero de decimal a octal
    en_octal = decimalToOctal(en_decimal);
    printf("Representación de octal a decimal mediante formateo: %o\n", en_decimal);
    printf("Conversión de octal a decimal mediante función %i\n", en_octal);

    return 0;
}
