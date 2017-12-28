#include <iostream>
#include <vector>

using namespace std;

/* Puedes pensar en un iterador como en un puntero de un elemento
el cual es parte de un contenedor más grande de elementos.

Para obtener el iterador apropiado a una clase plantilla de la
biblioteca estándar, usamos la siguiente sintaxis:
   std::nombre_de_clase<parametros_de_plantilla>::iterator variable
donde nombre_de_clase es el nombre del contenedor de la biblioteca
estándar que estamos usando.

Diferentes iteradores soportan diferentes tipos de comportamiento,
para ver una lista de los principales:
http://www.cplusplus.com/reference/iterator/
*/

int main() {
    vector<int> vectorDeEnteros;    // Creamos un vector
    vector<int>::iterator iterador; // Creamos el iterador
    // Añadimos elementos al vector
    vectorDeEnteros.push_back(1);
    vectorDeEnteros.push_back(3);
    vectorDeEnteros.push_back(2);

    // Implementación común (evitar)
    for (int i=0; i<vectorDeEnteros.size(); i++)
        cout << vectorDeEnteros[i] << "\n";

    cout << "\n";

    // Implementación de la biblioteca estándar
    for (iterador = vectorDeEnteros.begin();
    	     iterador != vectorDeEnteros.end();
    	     iterador++)
        cout << *iterador << "\n";  // Referencia como puntero

    return 0;
}


/* Fuentes:
https://www.cprogramming.com/tutorial/stl/iterators.html
http://www.cplusplus.com/reference/iterator/
*/