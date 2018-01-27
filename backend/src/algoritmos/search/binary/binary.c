#include <stdio.h>

#define LARGO 5 // Largo del array

unsigned long binary_search(long seq[], unsigned long n, long elem);
int main() {

    long array[LARGO] = {1, 3, 8, 16, 80};
    long elem = 16;
    long respuesta;

    respuesta = binary_search(array, LARGO, elem);
    if (respuesta == LARGO) {
        printf("El elemento %d no se encontró en el array.\n", elem);
    } else {
        printf("El número %d se encuentra en la posición %d.\n",
    	       elem, respuesta);
    }

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
