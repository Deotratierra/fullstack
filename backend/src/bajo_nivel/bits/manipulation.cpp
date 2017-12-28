#include <iostream>
#include <bitset>  // http://www.cplusplus.com/reference/bitset/bitset/
#include <string>

using namespace std;

// TRABAJO CON BITS, NÚMEROS BINARIOS

int main() {

    unsigned int dos = 2;
    unsigned int diez = 10;

    // Para representar números en binario
    cout << bitset<16>(dos) << endl; // Conjunto de 16 bits
    cout << bitset<32>(dos) << endl; // Conjunto de 32 bits
    cout << bitset<64>(dos) << endl; //             64 bits

    // Gracias al operador << podemos llevar el número 1 hacia
    // la izquierda la cantidad de veces que le indiquemos,
    // lo que en binario significa multiplicar por 2 elevado a
    // la cantidad de veces que movemos los unos
    dos = dos << 1;
    cout << dos << endl;   // 4
    cout << bitset<16>(dos) << endl << "______________________" << endl;

    cout << (diez <diez< 2) << endl;  // 10 * 2² = 10 * 4 = 40
    cout << bitset<8>(diez) << " ---> " << (bitset<8>(diez) << 2) << endl;
    cout << "______________________" << endl;

    // Por supuesto, gracias al operador >> realizamos la división opuesta
    int cuarenta = 40;
    cout << bitset<16>(cuarenta) << endl;
    cout << (cuarenta >> 3) << endl;  // 40 / 2³ = 40 / 8 = 8
    cout << "______________________" << endl;

    // Esta forma de operar es muchísimo más rápida que la usual

    // ------------------------------------------------------

    // Si realizamos la misma operación en caracteres
    char a = "a"[0];

    cout << bitset<8>(a) << endl;  // 01100001
    cout << (a << 1) << endl;      // 194
    cout << (a >> 1) << endl;      // 48
    cout << "______________________" << endl;


    // Si realizamos una operación que impliquen decimales
    unsigned int cinco = 5;

    cout << bitset<8>(cinco) << endl;
    cout << (cinco >> 1) << endl;  // 2  // ¿Debería dar 2.5?

    // Sólo funciona en enteros sin signo

    cout << "______________________" << endl;

    // ====================================================

    // Para convertir de binario a string
    cout << bitset<8>("a"[0]).to_string() << endl; // 01100001

    // Para convertir de binario a ulong
    cout << bitset<8>(96).to_ulong() << endl; // 96

    cout << "______________________" << endl;

    // ====================================================

    // Podemos operar como si los números binarios
    // fueran conjuntos de booleanos:

    char w = "w"[0];
    char h = "h"[0];

    // Operador &  (AND)
    cout << "w --> " << bitset<8>(w) << endl;
    cout << "h --> " << bitset<8>(h) << endl;
    cout << "--------------------------------------------" << endl;

    cout << bitset<8>(w) << " & " << bitset<8>(h) << " = " << bitset<8>(w & h);
    cout << " = " << (bitset<8>(w & h)).to_ulong() << endl;
        // 01110111 & 01101000 = 01100000 = 96

    cout << "--------------------------------------------" << endl;

    // Operador \  (OR)
    cout << bitset<8>(w) << " | " << bitset<8>(h) << " = " << bitset<8>(w & h);
    cout << " = " << (bitset<8>(w | h)).to_ulong() << endl;

    cout << "--------------------------------------------" << endl;

    // Operador ~
    // Este operador cambia todos los números por su contrario
    cout << " w --> " << bitset<8>(w) << endl << "~w --> " << bitset<8>(~w) << endl;

    return 0;

}


/* Fuentes:
https://katyscode.wordpress.com/2012/05/12/printing-numbers-in-binary-format-in-c/
https://www.cprogramming.com/tutorial/bitwise_operators.html
https://es.wikipedia.org/wiki/Operador_a_nivel_de_bits
https://es.wikipedia.org/wiki/C%C3%B3digo_binario
*/