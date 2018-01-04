#include <iostream>
#include <string>
#include <regex>

// El cabecero regex nació en la biblioteca Boost pero se convirtió
// en parte de la biblioteca estándar de C++ a partir de C++11

// Las expresiones regulares siguen la sintaxis ECMAScript:
// http://www.cplusplus.com/reference/regex/ECMAScript/

using namespace std;

int main() {

    string saludo1 = "Buenas tardes";
    string saludo2 = "Buenos días";

    // Crear una expresión regular
    regex expr{"\\w+\\s\\w+"};

    // -------------------------------------------

    // Comprobar si coincide
    bool encontrado1 = regex_match(saludo1, expr);
    bool encontrado2 = regex_match(saludo2, expr);
    // En el segundo caso, la tilde en la í elimina la coincidencia

    cout << boolalpha << encontrado1 << "\n";  // true
    cout << boolalpha << encontrado2 << "\n";  // false

    // boolalpha convierte un booleano en caracteres alfanuméricos:
    // (1 --> true, 0 --> false)

    // -------------------------------------------

    // Buscar una cadena por expresión regular
    regex expr2{"(\\w+)\\s(\\w+)"};
    smatch coinc;  // El objeto de coincidencias, donde se guardan los resultados
    if (regex_search(saludo1, coinc, expr2)) {
        cout << coinc[0] << "\n";                      // Buenas tardes
        cout << coinc[1] << "_" << coinc[2] << "\n";   // Buenas_tardes
    }

    // -------------------------------------------

    // Reemplazar caracteres en cadenas
    regex expr3{"\\s"};
    cout << regex_replace(saludo1, expr3, "-") << "\n";  // Buenas-tardes

    // -------------------------------------------

    return 0;
}

/* Fuentes:
http://www.cplusplus.com/reference/regex/
https://theboostcpplibraries.com/boost.regex
*/
