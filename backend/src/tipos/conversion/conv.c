#include <stdio.h>
#include <stdlib.h>

           //    CONVERSIONES ENTRE TIPOS EN C    //

int main() {
    // ===========================================================
    //                       CASTING
    /* El mecanismo del casting se usa cuando queremos convertir
        una expresión de un tipo a otro. Para ello, colocamos el tipo
        al cual queremos convertir una espresión antes de la misma
        entre paréntesis, tal que:
           (tipo) expresion
    */

    int a = 5, b = 3;
    float division1, division2, flotante1;

    // Conversión de enteros a flotantes
    division1 = (float) a / b;  // a se convierte a flotante antes de la división
    printf("%d / %d = %f\n", a, b, division1);  // 5 / 3 = 1.666667
    // El siguiente ejemplo es equivalente:
    flotante1 = (float) a;
    division2 = flotante1 / b;
    printf("%f / %d = %f\n\n", flotante1, b, division2);

    // ================================================================


    // ================================================================
    //                   PROMOCIÓN DE ENTEROS
    /* Es el proceso por el cual los valores de un entero de tipos "más pequeños"
    que int o unsigned int (por ejemplo char) son convertidos a int o unsigned int.
    */

    int i = 45, suma;
    char c = 'c';

    // Sumando int + char obtenemos un entero
    suma = i + c; // 109
    printf("i + c = %d\n\n", suma);

    // ================================================================


    // ================================================================
    //                 CONVERSIONES ARTIMÉTICAS USUALES

    /* Tomando el caracter c del ejemplo anterior, si lo imprimos
    formateado como flotante: */
    printf("%f\n\n", c);  // 5.000000

    /* Esto se debe a que el camino de conversión de tipos al cual realiza
    C automáticamente es el siguiente:
    int -> unsigned int > long -> long long -> unsigned long long -> float ->
    double -> long double
    */

    // ================================================================

    //            CONVERSIONES DE LA BIBLIOTECA ESTÁNDAR
    // https://es.wikipedia.org/wiki/Stdlib.h

    // Cadena de caracteres a flotante
    char* cadena1 = "3.49";
    float flotante2;

    flotante2 = atof(cadena1);
    printf("El número como cadena: %s\n", cadena1);
    printf("El número como flotante: %f\n\n", flotante2);

    // -----------------------------------------------------------

    // Cadena de caracteres a entero
    char* cadena2 = "3";
    int entero1;

    entero1 = atoi(cadena2);
    printf("El número como cadena: %s\n", cadena2);
    printf("El número como entero: %d\n\n", entero1);

    // ================================================================


    return 0;
}