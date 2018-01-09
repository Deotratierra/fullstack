#include <stdio.h>
#include <stdlib.h>  // La función strtol() se encuentra aquí


int main() {
    // Números en distintas bases
    char numeros[] = "2018 fbc45 -001101001111 0x6ffff";

    // ----------------------------------------------------------

    /* Convertir una cadena en su equivalente entero decimal especificando base


    Para ello usamos las funciones strtol() y strtoul():
    http://www.cplusplus.com/reference/cstdlib/strtol/

    Esta toma 3 parámetros posicionales:
    - Cadena de C empezando con una representación de un número entero.
    - Puntero a un objeto de tipo char, cuyo valor es establecido por la función
        al próximo catacter de la cadena después de la representación del valor numérico.
        Puede ser un puntero NULL, en cuyo caso no es usado.
    - Base numérica que determina los caracteres válidos y su interpretación.
        Si es 0, la base usada es determinada por el formato en la secuencia.
    */
    char *pFin;
    long int li1, li2, li3, li4;
    li1 = strtol(numeros, &pFin, 10);  // Decimal
    li2 = strtol(pFin, &pFin, 16);     // Hexadecimal
    li3 = strtol(pFin, &pFin, 2);      // Binario
    li4 = strtol(pFin, &pFin, 0);      // Automático
    printf("Los valores decimales equivalentes son: %d | %d | %d | %d\n", li1, li2, li3, li4);

    return 0;

}