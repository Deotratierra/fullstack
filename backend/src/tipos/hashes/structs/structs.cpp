#include <iostream>
#include <cstring>

using namespace std;

int main(){
    // Inicialización:
    struct alumno {
        char nombre[31];
        char direccion[40];
        unsigned long n_matricula;
        unsigned long telefono;
        float notas[10];
    };

    // Instanciación / definición:
    alumno alumno1, alumno2;

    // Podemos hacer ambas a la vez:
    struct _alumno {
        char nombre[31];
        char direccion[40];
        unsigned long n_matricula;
        unsigned long telefono;
        float notas[10];
    } alumno3, alumno4;

    // Para acceder a los miembros se utiliza el operador punto (.):
    alumno1.telefono = 943903456;
    strcpy(alumno1.direccion, "C/ Delicias 3, 1ºB");
    cout << alumno1.telefono << endl;  // 943903456
    cout << alumno1.direccion << endl; // C/ Delicias 3, 1ºB

}