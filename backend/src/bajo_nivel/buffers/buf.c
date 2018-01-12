#include <stdio.h>
#include <string.h>   // 
#include <stdlib.h>

/* Aclarar que el buffer no es un concepto exclusivo de C, ni hay
    ninguna forma de implemetarlo explícita. Reservar un espacio
    en memoria e ir iterando por los bloques significa manipular
    un buffer.
*/

int main() {
    // =======================================================
    //                       memset()
    /* Se usa para inicializar un número de bytes específico
        a un valor determinado dentro del buffer.
       Toma 3 parámetros:
           - Puntero a un área de memoria: el área de memoria a donde
               apunte el puntero pasado como primer parámetro será donde
               se establezcan los bytes.
           - Valor de los elementos: el segundo parámetro indica el valor
               que tomarán todos los elementos dentro de ese área de memoria.
           - Tamaño del área de memoria: el tercer parámetro requiere especificar
               el tamañ de memoria del área donde estamos trabajando.
    */
    int i;

    // Asignamos memoria para un array de 5 elementos
    char *a = (char *) malloc(5*sizeof(char));

    printf("Valores del buffer antes de ejecutar memset()\n");
    for (i = 0; i < 5; ++i)
        printf("  a[%d] = %d  ", i,    a[i]);

    // Establecemos el valor de todos los elementos del buffer a 3
    memset(a, 3, 5*sizeof(char));
    printf("\n\nValores después de ejecutar memset()\n");

    for (i = 0; i < 5; ++i)
        printf("  a[%d] = %d  ", i,    a[i]);
    printf("\n\n");

    // Liberamos el espacio asignado de la memoria
    free(a);

    return 0;
}
