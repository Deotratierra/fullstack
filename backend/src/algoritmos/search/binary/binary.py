#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search(array, query):
    lo, hi = (0, len(array) - 1)   # Índices menor y mayor en array
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # La mitad
        val = array[mid]           # Valor del índice a la mitad
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def main():
    array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
    print(array)
    print("Encontrado:", 5, "en el índice:", binary_search(array, 5))
    print("Encontrado:", -1, "en el índice:", binary_search(array, -1))

if __name__ == "__main__":
    main()