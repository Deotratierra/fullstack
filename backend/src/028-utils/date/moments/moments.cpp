#include <iostream>
// El siguiente tutorial está basado en bibliotecas de Boost
#include <boost/date_time/gregorian/gregorian.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>

using namespace std;
using namespace boost::gregorian;
using namespace boost::posix_time;

int main() {

    // =======   boost/date_time/gregorian/gregorian.hpp   =======

    // Crear fechas
    date fecha{2017, 12, 19};
    cout << fecha.year() << "\n";          // 2017
    cout << fecha.month() << "\n";         // Dec
    cout << fecha.day() << "\n";           // 19
    cout << fecha.day_of_week() << "\n";   // Tue
    cout << fecha.end_of_month() << "\n";  // 2017-Dec-31

    // Obtener el día actual (En UTC)
    date hoy = day_clock::universal_day();
    cout << hoy.day() << "\n";             // 19
    cout << hoy.month() << "\n";           // Dec
    cout << hoy.year() << "\n";            // 2017
        // Para obtener la fecha local usamos local_day()

    // --------------------------------------------------

    // Parsear cadena ISO a fecha
    date fecha2 = date_from_iso_string("20171219");
    cout << fecha2.day() << "\n";          // 19

    // --------------------------------------------------

    // Iterar por días, meses o años:
    // https://theboostcpplibraries.com/boost.datetime-calendar#ex.datetime_09

    // =============================================================


    // =======   boost/date_time/posix_time/posix_time.hpp   =======

    ptime marca_de_tiempo{fecha2, time_duration{12, 0, 0}};
    cout << marca_de_tiempo << "\n";               // 2017-Dec-19 12:00:00
    cout << marca_de_tiempo.date() << "\n";        // 2017-Dec-19
    cout << marca_de_tiempo.time_of_day() << "\n"; // 12:00:00

    // =============================================================


    return 0;
}

/* Fuentes:
https://theboostcpplibraries.com/boost.datetime-calendar
https://theboostcpplibraries.com/boost.datetime-location-independent-times
*/