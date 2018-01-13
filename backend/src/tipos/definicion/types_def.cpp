using namespace std;

int main() {
    // Designar nuevos nombres a tipos existentes:
    typedef unsigned long ulong; // Designamos al tipo unsigned long el nombre ulong

    typedef int nota_alumno_t;
    nota_alumno_t nota;         // Ahora...
    nota = 100;                 // <-- esto...
    int _nota = 100;            // <-- es lo mismo que esto.

    /* Esto se usa, por ejemplo, creando código en C++ para Python:
    https://docs.python.org/3/extending/newtypes.html */

    return 0;

}
