#include <stdio.h>
#include <time.h>

int main() {

    /* Obtener el número de pulsos de reloj desde que se inició el proceso

    Los pulsos de reloj son unidades que usan los dispositivos electrónicos para
    medir el tiempo. Para los ordenadores personales, los pulsos de reloj generalmente
    se refieren al reloj principal del sistema, el cual corre a 66 MHz. Esto significa
    que hay 66 millones de pulsos (o ciclos) de reloj por segundo. */
    clock_t pulsos;  // clock_t es el tipo que retorna clock()
    pulsos = clock();
    printf("Pulsos de reloj desde el comienzo del proceso: %d\n", pulsos);
    /* Para calcular la relación entre los pulsos de reloj y los segundos reales,
        podemos dividir el tiempo retornado por clock entre la variable
        CLOCKS_PER_SEC que nos provee esta biblioteca. */
    clock_t equiv_segundos;
    equiv_segundos = ((double)pulsos)/CLOCKS_PER_SEC;
    printf("Tiempo usado por la CPU en seg = %f (%d µs).\n\n",
        equiv_segundos, equiv_segundos*1000000);

    return 0;
}