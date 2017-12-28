#include <iostream>
#include <string>

// Este tutorial incluye bibliotecas Boost
#include <boost/format.hpp>

using namespace std;

int main() {

	// ===================   printf   ===========================
	// Sirve para imprimir información formateada
	// Lista de marcadores: http://www.cplusplus.com/reference/cstdio/printf/

	// Precedido de ceros y eliminando caracteres
    printf ("%10d %Ld \n", 19, 30000L);  //         19 30000

    // Cadenas
    printf ("%s \n", "Cadena");          // Cadena

    // Flotantes
    printf ("%4.2f %+.0e %E \n", 3.1416, 3.1416, 3.1416);  // 3.14 +3e+00 3.141600E+00

	// ==========================================================


	// =============   boost/format.hpp   ================

    // Salida formateada
    cout << boost::format{"%1%/%2%/%3%"} % 19 % 12 % 2017 << "\n";  // 19/12/2017
    cout << boost::format{"%2%/%1%/%3%"} % 19 % 12 % 2017 << "\n";  // 12/19/2017

    cout << boost::format{"%|1$+| %2% %1%"} % 1 % 2 << '\n';        // +1 2 1
    cout << boost::format{"%|+| %|| %||"} % 1 % 2 % 1 << '\n';      // +1 2 1

    // Con la función printf(), imprimir valores numéricos como cadenas
    // no es posible, pero con boost se puede:
    std::cout << boost::format{"%+s %s %s"} % 1 % 2 % 1 << '\n';    // +1 2 1

    // ===================================================

	return 0;
}

/* Fuentes:
https://theboostcpplibraries.com/boost.format
http://www.cplusplus.com/reference/cstdio/printf/
*/
