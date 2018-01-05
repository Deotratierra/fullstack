#include <iostream>

using namespace std;

//  CANALES EN C++  //

int main() {
    /* En C++ las tres salidas estándar se localizan en el cabecero iostream
    y se denominan cin, cout y cerr.
    Los operadores de direccionamiento son los encargados de manipular el flujo de datos
    desde o hacia el dispositivo referenciado por un canal específico. El salidas es <<
    y el de entradas es >>

    =======================================================================================

    Para manipular la salida estándar existen ciertos indicadores. Para una lista completa:
    https://doc.bccnsoft.com/docs/cppreference_en/io_flags.html
    El siguiente es un ejemplo: */

    // Mostrar la salida en valores booleanos (por defecto  cout << true  produce 1):
    cout << boolalpha << true << endl;  // true

    /* Podemos establecer este comportamiento por defecto sin especificarlo cada vez que lo
      necesitamos por medio de la función setf()  */
    cout.setf(ios::boolalpha);
    cout << true << endl;


    return 0;
}

/* Fuentes:
https://es.wikibooks.org/wiki/Programaci%C3%B3n_en_C%2B%2B/Streams
*/