#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubble_sort(array):

    def intercambiar(i, j):
        array[i], array[j] = array[j], array[i]

    n = len(array)
    intercambiado = True
    while intercambiado:
        intercambiado = False
        for i in range(1, n):
            if array[i - 1] > array[i]:
                intercambiar(i - 1, i)
                intercambiado = True

if __name__ == "__main__":
    array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
             4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    print(array)
    bubble_sort(array)
    print(array)
