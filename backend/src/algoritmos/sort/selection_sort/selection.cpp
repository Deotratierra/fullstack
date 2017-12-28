#include <iostream>

using namespace std;

// ============     ALGORITMO     ==============

template <typename Type>
void selection_sort(Type *seq, ulong n) {
    // Ordena lista[] (en orden ascendente)
    Type temp;  // elemento temporal (usado al final)
    for (ulong i=0; i<n; ++i) {
        Type elem = seq[i];
        ulong min = i;   // índice del mínimo
        ulong j = n;
        while ( --j > i ) { // Busca el índice del mínimo elemento
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
};

// ============     TESTING     ==============

template <typename Type>
bool is_sorted(const Type *seq, ulong n) {
    // Retorna si la secuencia
    for (ulong i=1; i<n; ++i){
    if (seq[i-1] > seq[i]) { return false; };
    }
    return true;
}


// ============================================

main() {

    int lista[4] = {22, 2, 44, 4};
    cout << "Array desordenado:" << endl;
    for (const auto& i : lista) {
        cout << i << " ";
    }
    cout << endl << endl;

    selection_sort(lista, 4);

    if (is_sorted(lista, 4)){
        cout << "Array ordenado:" << endl;
        for (const auto& i : lista) {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
};
