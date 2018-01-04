#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
    char nombre[30];
    cout << "Escribe tu nombre: ";
    //cin >> nombre; // <----- No funciona si hay un espacio en el nombre
    gets(nombre);
    /* ^^^ Roba memoria fuera de su espacio si la
           cadena introducida supera la longitud
           de la variable nombre (30 caracteres) */

    cout << "Bienvenid@ al curso, " << nombre << ".";
    return 0;
}
