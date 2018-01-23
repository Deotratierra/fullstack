#include <stdio.h>
#include <time.h>


typedef unsigned long ulong;

ulong factorial(ulong n);

int main() {
    /* Para calcular el tiempo que toma un trozo de código
        en C, podemos usar la función clock, dentro del cabecero
        <time.h>, que devuelve un float de tipo clock_t */

    ulong resultado;
    double tiempo;

    // Envolvemos la función a cronometrar entre marcas de tiempo
    clock_t start = clock();
    resultado = factorial(600);
    clock_t end = clock();

    // Si queremos obtener el tiempo en segundos dividimos
    // por la variable CLOCKS_PER_SEC
    tiempo = (double)(end - start);// / CLOCKS_PER_SEC;

    printf("Tiempo empleado en la función: %f µs (microsegundos)\n", tiempo);

    return 0;
}

/**
 * Calcula el factorial de un número
 * @param  n Número a calcular
 */
ulong factorial(ulong n) {
    if (n == 1) {
        return 1;
    } else {
        return n*factorial(n-1);
    }
}


/* Fuentes:
https://stackoverflow.com/questions/5248915/execution-time-of-c-program
*/

