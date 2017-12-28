#include <iostream>
#include <thread>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Vector de workers
    vector<thread> workers;

    for (int i=1; i<6; i++) {
        // Los hilos pueden tomar una función lambda
        workers.push_back(thread( [i]() {
            cout << "Dentro del hilo número " << i << "\n";
        }));
    }

    // Esperamos a finalizar todos los hilos
    for_each(workers.begin(), workers.end(), [](thread &t) {
        t.join();
    });

    // Los hilos se ejecutan de forma desordenada

    return 0;
}