#include <iostream>

using namespace std;

// ============     ALGORITMO     ==============

template<typename Type>
void bubble_sort(Type seq[], ulong n) {
    // Aplica el algoritmo de ordenamiento de burbuja
    // Necesita un array de elementos y el largo del array como parámetros
    bool intercambiado;
    int i, temp;
    do {
        intercambiado = false;
        for(i=1; i <= n; i++) {
            if (seq[i-1] > seq[i]) {
                temp = seq[i];
                seq[i] = seq[i-1];
                seq[i-1] = temp;
                intercambiado = true;
            }
        }
    } while(intercambiado);
}

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

int main() {
    int lista[11] = {1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100};
    cout << "Array desordenado:" << endl;
    for (const auto& i : lista) {
        cout << i << " ";
    }
    cout << endl;

    bubble_sort(lista, 11);

    if (is_sorted(lista, 4)){
        cout << "Array ordenado:" << endl;
        for (const auto& i : lista) {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}
