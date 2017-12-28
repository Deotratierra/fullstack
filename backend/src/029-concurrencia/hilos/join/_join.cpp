#include <iostream>
#include <thread>
#include <chrono>

// Para compilar, linkear con -pthread:
// g++ th.cpp -o t -pthread

using namespace std;

void dormir(int segundos) {
    this_thread::sleep_for(chrono::seconds(segundos));
}

// Función que se ejecuta al crear el hilo
void contador() {
    for (int i=1; i<6; ++i) {
        cout << i << "\n";
        dormir(1);
    }
}

int main() {
    // Crear hilos
    thread t1{contador};
    thread t2(contador);

    // Esperamos a que terminen los hilos
    t1.join();
    t2.join();

    cout << "Fin de la ejecución" << "\n";

    return 0;
}

/* Fuentes:
http://www.cplusplus.com/reference/thread/thread/
http://www.cplusplus.com/reference/thread/this_thread/sleep_for/
https://solarianprogrammer.com/2011/12/16/cpp-11-thread-tutorial/
*/