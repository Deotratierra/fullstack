#include <iostream>
#include <string>
#include <exception>

using namespace std;

// MANEJO DE EXCEPCIONES EN C++

int main() {
    // =============   CAZAR EXCEPCIONES   =================

    string saludo = "Hola";

    /* El control de excepciones en C++ se realiza mediante
    las sentencias try - catch */
    try {
        cout << saludo.at(100) << endl;  // Intentamos acceder al índice 100
    } catch (exception& ex) {
        cout << ex.what() << endl;
    };  // basic_string::at: __n (which is 100) >= this->size() (which is 4)


    /* La clase exception usada para cazar el error
    se encuentra en la biblioteca estándar exception:
    http://www.cplusplus.com/reference/exception/exception/

    En el enlace anterior se encuentra una lista con las excepciones
    definidas en la biblioteca estándar.

    Gracias a la función what() podemos acceder a la cadena de texto
    que identifica el error:
    http://www.cplusplus.com/reference/exception/exception/what/

    Existen otras excepciones en la biblioteca estándar, dentro del cabecero
    stdexcept: http://www.cplusplus.com/reference/stdexcept/
    */

    // =============   EXCEPCIONES PERSONALIZADAS   =================
    /* Lo más simple sería sobreescribir el método what() de la clase
    exception para indicar el motivo del error */

    class ZeroDivisionError : public exception {
        const char* what() const throw() {
            return "Error: División entre 0";
        }
    };

    double numerador = 15,
           denominador = 0;

    try {
    	if (denominador == 0) { throw ZeroDivisionError(); }
    	cout << numerador << " / " << denominador << " = " << numerador/denominador << endl;
    } catch (exception& ex) {
    	cout << ex.what() << endl;  // Error: División entre 0
    };

    return 0;
}

/* Fuentes:
https://es.wikibooks.org/wiki/Programaci%C3%B3n_en_C%2B%2B/Excepciones
*/
