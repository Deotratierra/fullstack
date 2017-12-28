#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

// mutex es el objeto que crea los locks
mutex m;  // abrebiatura de "mutual exclusion"

int usos = 0;

void WC() {
    m.lock();  // Cuando entramos al baño cerramos el pestillo
    usos++;  // Ningún otro thread puede acceder ahora a la variable usos
    cout << usos << " haciendo sus necesidades\n";
    m.unlock();  // Terminamos, abrimos el baño de nuevo
}

int main () {
    // Imagina que los siguientes threads son una multitud de
    // personas haciendo cola para entrar a un baño público
    thread hombre(WC);
    thread anciano(WC);
    hombre.join();
    anciano.join();

    // Con exclusiones mutuas, los threads no se ejecutan en paralelo,
    // si no que bloquean la ejecución

    return 0;
}

/* Fuentes:
https://stackoverflow.com/questions/4989451/mutex-example-tutorial
http://nrecursions.blogspot.com.es/2014/08/mutex-tutorial-and-example.html
https://es.wikipedia.org/wiki/Exclusi%C3%B3n_mutua_(inform%C3%A1tica)
*/