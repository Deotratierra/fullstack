#include <stdio.h>
#include <math.h>

/* Para linkear la biblioteca <math.h> usamos la opción '-lm'
$ gcc aritmetica.c -o aritmetica -lm
*/

int main() {
    float num, calc;
    printf("Introduce un número: ");
    scanf("%f", &num);
    printf("\n");

    // Raíz cuadrada
    if (num > 0) {
        calc = sqrt(num);
        printf("\tRaíz cuadrada = %.2f\n", calc);
    }

    // Próximo entero hacia arriba
    calc = ceil(num);
    printf("\tPróximo entero hacia arriba = %.2f\n", calc);

    // Próximo entero hacia abajo
    calc = floor(num);
    printf("\tPróximo entero hacia abajo = %.2f\n", calc);

    // Valor absoluto
    calc = fabs(num);
    printf("\tValor absoluto = %.2f\n", calc);

    // Logaritmo natural
    calc = log(num);
    printf("\tLogaritmo natural = %.2f\n", calc);

    // Logaritmo en base 10
    calc = log10(num);
    printf("\tLogaritmo en base 10 = %.2f\n", calc);

    return 0;
}

/* Fuentes:
https://es.wikipedia.org/wiki/Math.h
*/
