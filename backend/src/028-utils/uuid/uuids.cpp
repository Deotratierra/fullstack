#include <iostream>

// El siguiente ejemplo está basado en bibliotecas Boost:
#include <boost/uuid/uuid.hpp>
#include <boost/uuid/uuid_generators.hpp>
#include <boost/uuid/uuid_io.hpp>

using namespace std;

int main() {
    // Generador aleatorio
    boost::uuids::random_generator gen;

    // Identificador
    boost::uuids::uuid identificador = gen();

    cout << identificador << "\n";

}

/* Fuentes:
https://theboostcpplibraries.com/boost.uuid
*/
