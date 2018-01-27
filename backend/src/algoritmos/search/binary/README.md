## Búsqueda binaria
El algoritmo de búsqueda binaria funciona para un array ordenado.

### Funcionamiento
Compara el valor con el elemento en el medio del array. Si no son iguales, la mitad en el cual el valor no puede estar es eliminada y la búsqueda continúa en la mitad restante hasta que el valor se encuentra.

### Coste
En el peor de los casos `T(n) = O(log n)`.