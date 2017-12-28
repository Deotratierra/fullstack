#include <iostream>
#include <chrono>

// Este tutorial incluye bibliotecas Boost
#include <boost/date_time/gregorian/gregorian.hpp>

using namespace std;
//using namespace std::chrono;  // chrono tiene su propio espacio de nombres
using namespace boost::gregorian;

// No olvides compilar con la instrucción -std=c++11   (o superior)



/*
C++ incluye soporte para la manipulación del tiempo mediante dos vías:
  - La biblioteca chrono, es una colección de tipos que manipulan el tiempo
    con diferentes grados de precisión (por ejemplo std::chrono::time_point).
  - La biblioteca con las funciones clásicas estilo C de fecha y hora
    (por ejemplo std::time).
 */

int main() {
    // ===================   chrono   ==========================
    /* Para manejar tiempos, este header utiliza tres conceptos:
    - Duraciones:
        Miden espacios de tiempos, como un minuto, dos horas o diez milisegundos.
        En esta biblioteca están representados como objetos de la clase duration.
    - Puntos en el tiempo:
        Referencia a un punto específico en el tiempo. Es esta biblioteca están
        representados como objetos de la clase time_point
    - Relojes:
        Un framework que relaciona un punto en el tiempo a un tiempo físico real.
        La bibilioteca provee al menos 3 relojes para expresar el tiempo actual como
        time_point:system_clock, steady_clock y high_resolution_clock
    */

    // ----------------------------------------------------------

    // Durations:
        // http://es.cppreference.com/w/cpp/chrono/duration

    typedef chrono::duration<int> segundos;  // Definiendo tipos
    typedef chrono::duration<int, milli> milisegundos;

    segundos segundos_por_dia (60*60*24);
    cout << segundos_por_dia.count() << "\n";   // 86400

    milisegundos milisegundos_por_minuto (1*1000*60);
    cout << milisegundos_por_minuto.count() << "\n";  // 60000

                                            // Sin definir tipos
    chrono::hours dia(24);
    cout << dia.count() << "\n";  // 24

    chrono::minutes minutos_por_dia(dia);  // Podemos pasarle un objeto duración
    cout << minutos_por_dia.count() << "\n";  // 1440

    // ===========================================================


    // =======   boost/date_time/gregorian/gregorian.hpp   =======

    // Duración entre fechas:
    date fecha1{2017, 1, 31};
    date fecha2{2017, 5, 15};
    date_duration diferencia = fecha2 - fecha1;
    // Así también:
    //     date_period periodo{fecha1, fecha2};
    //     date_duration diferencia = periodo.length();
    cout << diferencia.days() << "\n";  // 104

    // Semanas:
    weeks semanas{4};
    cout << semanas.days() << "\n";  // 28

    // Meses:
    months meses{3};
    cout << meses.number_of_months() << "\n";  // 3

    // Años
    years anatemas{5};
    cout << anatemas.number_of_years() << "\n"; // 5
    // Los meses y los años tienen diferente número de días,
    // por lo cual no nos permite consultarlos.

    // ==========================================================


	return 0;
}

/*
http://es.cppreference.com/w/cpp/chrono/duration
https://theboostcpplibraries.com/boost.datetime-calendar
 */