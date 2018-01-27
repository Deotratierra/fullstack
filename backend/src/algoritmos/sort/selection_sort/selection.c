#include <stdio.h>

void selection_sort(long seq[], unsigned long n);

int main() {
    long array[11] = {1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100};

    printf("Array desordenado: ");
    for (int i=0; i < 11; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    selection_sort(array, 11);

    printf("Array ordenado: ");
    for (int i=0; i < 11; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");


    return 0;
}

/**
 * Ordena un array de tipo long
 * según el algoritmo de ordenación de selección
 * @param seq Array de números enteros
 * @param n   Número de elementos en el array
 */
void selection_sort(long seq[], unsigned long n) {
    long elem, temp;
    unsigned long min, j;
    for (long i=0; i<n; ++i) {
        elem = seq[i];
        min = i;
        j = n;
        while (--j > i) {
            if (seq[j] < elem) {
                min = j;
                elem = seq[min];
            }
        }
        if (min != i) {
            temp = seq[i];
            seq[i] = seq[min];
            seq[min] = temp;
        }
    }
}