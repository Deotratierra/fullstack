#include <string>
#include <vector>
#include <iostream>

// Este tutorial está basado en las bibliotecas Boost
#include <boost/algorithm/string/case_conv.hpp>
#include <boost/algorithm/string/erase.hpp>
#include <boost/algorithm/string/join.hpp>
#include <boost/algorithm/string/replace.hpp>
#include <boost/locale/conversion.hpp>


using namespace std;
using namespace boost::algorithm;
using namespace boost::locale;

int main(){

    // ============================================================

    // Biblioteca estándar

    // Recorrer una cadena
    int index = 0;
    while (index < fruit.length()) {
        char letter = fruit[index];
        cout << letter << endl;
        index += 1;
    }

	// =========   boost/algorithm/string/case_conv.hpp   =========

	string s = "Boost C++ Libraries";

    // Copia de cadena a mayúsculas
    cout << to_upper_copy(s) << "\n";  // BOOST C++ LIBRARIES

    // Copia de cadena a minúsculas
    cout << to_lower_copy(s) << "\n";  // boost c++ libraries

    // Ambas funciones retornan una copia de la cadena original,
    // por lo cual aún conservamos la original:
    cout << s << "\n";  // Boost C++ Libraries

    // Convertir cadena a mayúsculas
    to_upper(s);
    cout << s << "\n";  // BOOST C++ LIBRARIES

    // Convertir cadena a minúsculas
    to_lower(s);
    cout << s << "\n";  // boost c++ libraries

    // ===========================================================


    // =========   boost/algorithm/string/erase.hpp   =========

    string saludo = "Hola, ¿que tal estás?";

    // Eliminar primera subcadena que conincida con otra pasada como argumento
    cout << erase_first_copy(saludo, "a") << "\n";   // Hol, ¿que tal estás?
    erase_first(saludo, "o");
    cout << saludo << "\n";                          // Hla, ¿que tal estás?

    // Eliminar última subcadena que concida con otra pasada como argumento
    cout << erase_last_copy(saludo, "o") << "\n";    // Hla, ¿que tal estás?
    erase_last(saludo, "a");
    cout << saludo << "\n";                          // Hla, ¿que tl estás?

    // Eliminar subcadena n pasada como argumento
    cout << erase_nth_copy(saludo, "e", 1) << "\n";  // Hla, ¿que tl stás?
    erase_nth(saludo, "es", 0);
    cout << saludo << "\n";                          // Hla, ¿que tl tás?

    // Eliminar n primeros caracteres una cadena
    cout << erase_head_copy(saludo, 3) << "\n";      // , ¿que tl tás?
    erase_head(saludo, 3);
    cout <<  saludo << "\n";                         // , ¿que tl tás?

    // Eliminar n últimos caracteres de una subcadena pasada como argumento
    cout << erase_tail_copy(saludo, 2) << "\n";     // , ¿que tl tá
    erase_tail(saludo, 2);
    cout << saludo << "\n";                         // , ¿que tl tá

    // ========================================================


    // =========   boost/algorithm/string/join.hpp   ==========

    // Concatenar cadenas
    vector<string> lista = {"Álvaro", "Mondéjar"};
    cout << join(lista, " ") << "\n";  // Álvaro Mondéjar
    string nombre = join(lista, " ");

    // ========================================================


    // =========   boost/algorithm/string/replace.hpp   ==========

    // Reemplazar subcadenas
    // Todas las funciones tienen su homóloga sin _copy
    cout << replace_first_copy(nombre, "M", "-") << '\n';    // Álvaro -ondéjar
    cout << replace_nth_copy(nombre, "o", 1, "O") << '\n';   // Álvaro MOndéjar
    cout << replace_last_copy(nombre, "a", "A") << '\n';     // Álvaro MondéjAr
    cout << replace_all_copy(nombre, "r", "R") << '\n';      // ÁlvaRo MondéjaR
    cout << replace_head_copy(nombre, 7, "Antonio") << '\n'; // Antonio Mondéjar
    cout << replace_tail_copy(nombre, 9, "García") << '\n';  // Álvaro García

    // ===========================================================

    // Trims, comparaciones, splitting, searching... en la fuente

    return 0;

}

/* Fuente:
https://theboostcpplibraries.com/boost.stringalgorithms
*/
