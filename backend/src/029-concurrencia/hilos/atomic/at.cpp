#include <iostream>
#include <thread>
#include <atomic>

using namespace std;

/* El cabecero atomic (en la biblioteca estándar desde C++11,
   antes también incluido en las bibliotecas Boost) nos permite
   acceder al mismo espacio de memoria entre diferentes threads.

   Funciona porque algunos procesadores permiten acceso atómico
   en variables, en caso de no, usa automáticamente locks.
*/

atomic<int> a = {0};

void aumentar() {
    ++a;
}

int main() {
    thread t1{aumentar};
    thread t2{aumentar};
    t1.join();
    t2.join();

    cout << a << "\n";  // 2

    return 0;
}

/* Fuentes:
http://www.cplusplus.com/reference/atomic/
https://theboostcpplibraries.com/boost.atomic
http://preshing.com/20130618/atomic-vs-non-atomic-operations/
*/

