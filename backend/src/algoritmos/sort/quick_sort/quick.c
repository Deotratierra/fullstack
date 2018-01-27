#include <stdio.h>

void quick_sort(long seq[], unsigned long n);

void qs(long seq[], long left_limit, long right_limit);

int main() {
    long array[11] = {1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100};

    printf("Array desordenado: ");
    for (int i=0; i < 11; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    quick_sort(array, 11);

    printf("Array ordenado: ");
    for (int i=0; i < 11; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}

/**
 * Ordena un array de tipo long
 * según el algoritmo de ordenación rápido
 * @param seq Array de números enteros
 * @param n   Número de elementos en el array
 */
void quick_sort(long seq[], unsigned long n) {
    qs(seq, 0, n-1);
}

void qs(long seq[], long left_limit, long right_limit) {
    long left, right, temp, pivot;

    left = left_limit;
    right = right_limit;
    pivot = seq[(left+right)/2];

    while (left<=right) {
        while (seq[left] < pivot && left < right_limit) {
        	left++;
        }
	    while (pivot < seq[right] && right > left_limit) {
	    	right--;
	    }
	    if (left <= right) {
	        temp = seq[left];
	        seq[left] = seq[right];
	        seq[right] = temp;
	        left++;
	        right--;
	    }
    }
    if (left_limit < right) {
    	qs(seq, left_limit, right);
    }
	if (right_limit > left) {
		qs(seq, left, right_limit);
	}
}
