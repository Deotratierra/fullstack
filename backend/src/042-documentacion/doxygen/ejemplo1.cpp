#include <iostream>

using namespace std;

// El primer bloque de comentarios debe llevar doble asterisco

/**
 * @brief Suma dos números enteros.
 * @param a Primer entero a sumar
 * @param b Segundo entero a sumar
 * @return Un nuevo entero a+b
 */
int sumar(int a, int b){
    return a + b;
}

int main() {
    int resultado = sumar(7, 8);
    cout << "El resultado de la suma es " << resultado << endl;

    return 0;
}
