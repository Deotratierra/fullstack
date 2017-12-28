#include <iostream>
#include <chrono>

using namespace std;

int main() {
    // =================================================================
    // Para cronometrar el tiempo que ha pasado entre dos puntos
    // del programa lo más simple sería usar el siguiente código

    // Creamos un punto de comienzo en unix timestamps
    //     La función now() del reloj de alta resolución de la biblioteca
    //     chronos es estática, por lo que no hace falta instanciar el reloj
    auto start = chrono::high_resolution_clock::now();

    // ...
    // Nuestro código aquí
    // ...

    // Punto final
    auto end = chrono::high_resolution_clock::now();
    // Calculamos la duración entre ambos puntos
    chrono::duration<double> seconds_diff = end - start; // En segundos
    chrono::duration<double, milli> miliseconds_diff = end - start; // En milisegundos

    cout << "Segundos: " << seconds_diff.count() << endl;
    cout << "Milisegundos: " << miliseconds_diff.count() << endl;


    // ================================================================


	return 0;
}

/* Fuentes:
https://www.pluralsight.com/blog/software-development/how-to-measure-execution-time-intervals-in-c--
*/
