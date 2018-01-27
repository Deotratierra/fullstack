## Ordenamiento rápido (quicksort)
Este algoritmo no deja obsoletos otros más simples, debido a que para arrays pequeños, los algoritmos más simples suelen ser más rápidos debido a su sobrecarga de contabilidad mínima.

La principal tarea que realiza el quicksort es dividir el array. La rutina reordena el array y retorna un índice pivote `p` tal que `max(i_0, ..., i_p-1) <= min(i_p, ..., i_n-1)`.

Posee una complejidad de `O(n log(n))` en el caso más rápido.
