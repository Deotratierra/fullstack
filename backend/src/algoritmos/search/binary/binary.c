#include <stdio.h>
#include <stdlib.h>  // bsearch()

#define LARGO 5 // Largo del array

// Inicialización de funciones
unsigned long binary_search(long seq[], unsigned long n, long elem);
int cmpfunc(const void * a, const void * b);

int main() {

    long array[LARGO] = {1, 3, 8, 16, 80};
    long elem = 16;
    long respuesta1;

    // Implementación manual
    respuesta1 = binary_search(array, LARGO, elem);
    if (respuesta1 == LARGO) {
        printf("El elemento %d no se encontró en el array.\n", elem);
    } else {
        printf("El número %d se encuentra en la posición %d.\n",
    	       elem, respuesta1);
    }

    // =================================================================

    /* bsearch()                                    <stdlib.h>

    void *bsearch(const void *key, const void *base, size_t nitems,
                  size_t size, int (*compar)(const void *, const void *))

    En la biblioteca estándar de C existe una función llamada bsearch()
    que realiza la búsqueda binaria. Los parámetros que toma son:
        1. Puntero al elemento a buscar (haciendo casting a void*).
        2. Array.
        3. Número de elementos en el array.
        4. Tamaño de cada elemento del array.
        5. Una función de comparación que toma como parámetros dos punteros
            haciendo un casting a void*. Para buscar un elemento se restan
            ambas direcciones de memoria.
        Devuelve un puntero al elemento si lo encuentro, en caso contrario
            devuelve NULL.

    Sirve para buscar rápidamente si un elemento se encuentra en un conjunto.
    */
    long *respuesta2;

    respuesta2 = bsearch(&elem, array, LARGO, sizeof(long), cmpfunc);
    if (respuesta2 != NULL) {
        printf("El elemento %d fue encontrado.\n", *respuesta2);
    } else {
        printf("El elemento %d no fue encontrado.\n", elem);
    }

    // =================================================================

    return 0;
}

/**
 * Devuelve el índice del primer elemento
 *   encontrado en un array long. Si el elemento
 *   no se encuentra devuelve el largo del array.
 * @param  seq  Array de enteros long
 * @param  n    Número de elementos en el array
 * @param  elem Elemento a buscar en el array
 * @return      Índice de la posición del elemento encontrado
 */
unsigned long binary_search(long seq[], unsigned long n, long elem) {
    unsigned long lowest = 0,
                  highest = n-1,
                  temp;
    while (lowest != highest) {
        temp = (highest + lowest) / 2;
        if (seq[temp] < elem) {
            lowest = temp + 1;
        } else {
            highest = temp;
        }
    }
    if (seq[highest] == elem) {
        return highest;
    } else {
        return n;
    }
}


int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
