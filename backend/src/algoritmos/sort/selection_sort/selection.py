#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==========     ALGORITMO     ============

def selection_sort(seq):
    """Ordena lista (en orden ascendente)"""
    seqlen = len(seq)
    for i in range(seqlen):
        mininum = seq[i]
        j = seqlen - 1
        while j > i:
            if seq[j] < seq[i]:
                minimun = j
                elem = seq[minimun]
            j -= 1
        if mininum != i:
            temp = seq[i]
            seq[i] = seq[minimun]
            seq[minimun] = temp
    return seq

# ==========     TESTING     ============

def is_sorted(seq):
    seqlen = len(lista) - 1
    for i in range(seqlen):
        i += 1
        if seq[i-1] > seq[i]: return False
    return True

# ============================================

if __name__ == "__main__":
    lista = [22, 2, 44, 4]
    print("Array desordenado:")
    print(lista)

    lista_ordenada = selection_sort(lista)
    if is_sorted(lista_ordenada):
        print("Array ordenado:")
        print(lista_ordenada)
