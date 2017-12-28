#include <iostream>

using namespace std;

template <typename Type>
ulong binary_search(const Type *seq, ulong n, const Type elem) {
    // Devuelve el índice del primer elemento en seq que es igual
    // a elem. seq debe estar ordenada en orden ascendente
    ulong lowest = 0, highest = n-1;
    while (lowest != highest) {
        ulong temp = (highest + lowest) / 2;

        if (seq[temp] < elem) { lowest = temp + 1; }
        else { highest = temp; }
    }
    if (seq[highest] == elem) { return highest; }
    else { return n; }
}

main() {
    int lista[5] = {1, 2, 3, 4, 5};
    int elem = 4;
    int response = binary_search(lista, 5, elem);
    cout << "El elemento " << elem;
    cout << " se encuentra en la posición " << response << endl;

    return 0;
}
