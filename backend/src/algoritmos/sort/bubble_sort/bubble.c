#include <stdio.h>

/**
 * Ordena un array de enteros largo
 * según el algoritmo de ordenación de burbuja
 * @param seq Array de números enteros
 * @param n   Número de elementos en el array
 */
void bubble_sort(long seq[], unsigned long n) {
    char intercambiado = 1;
    int i, temp;
    while (intercambiado == 1) {
        intercambiado = 0;
        for (i=1; i<=n; i++) {
            if (seq[i-1] > seq[i]) {
                temp = seq[i];
                seq[i] = seq[i-1];
                seq[i-1] = temp;
                intercambiado = 1;
            }
        }
    }
}

int main() {
    long array[11] = {1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100};

    printf("Array desordenado: ");
    for (int i=0; i < 11; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    bubble_sort(array, 11);

    printf("Array ordenado: ");
    for (int i=0; i < 11; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}