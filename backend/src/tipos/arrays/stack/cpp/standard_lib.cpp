#include <iostream>
#include <stack>   // Para usar las pilas la incluimos.
                   // Se encuentran en la bibliopteca estándar:
                   // http://www.cplusplus.com/reference/stack/stack/

using namespace std;

int main() {

    stack <int> pila;

    // Insertar un elemento en la pila:
    pila.push(10);

    // Devolver el último elemento sin eliminarlo:
    cout << "Último elemento en la pila " << pila.top() << endl;

    pila.push(30);

    // COnsultar el número de elementos en la pila:
    cout << "Tamaño de la pila: " << pila.size() << endl;
    cout << "Último elemento en la pila " << pila.top() << endl << endl;

    // Eliminar el último elemento de la pila (no lo devuelve)
    pila.pop();
    cout << "Sacamos el último elemento de la pila" << endl;
    cout << "Tamaño de la pila: " << pila.size() << endl;
    cout << "Último elemento en la pila: " << pila.top() << endl << endl;

    stack <int> pila2;
    pila2.push(55);

    cout << "Intercambiamos el contenido entre dos pilas" << endl;
    // Intercambiar contenido entre dos pilas
    pila2.swap(pila);

    cout << "Último elemento en la pila: " << pila.top() << endl << endl;

    pila.pop();
    // Saber si está vacía una pila
    cout << "¿Está vacía la pila (1 = SI, 2 = NO)? " << pila.empty() << endl << endl;

	return 0;
}