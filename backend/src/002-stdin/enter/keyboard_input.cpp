#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
    char name[30];
    cout << "Escribe tu nombre: ";
    //cin >> name; // <----- No funciona si hay un espacio en el nombre
    gets(name);
    /* ^^^ Roba memoria fuera de su espacio si la
           cadena introducida supera la longitud
           de la variable name (30 caracteres) */

    cout << "Bienvenid@ al curso, " << name << ".";
    return 0;
}
