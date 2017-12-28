#include <iostream>
#include <fstream>

/* C++ provee las siguientes clases para ejecutar
   salidas y entradas de caracteres con archivos:
       - ofstream: Escribir en archivos
       - ifstream: Leer archivos
       - fstream: Ambas operaciones
*/

using namespace std;

int main() {
    // Abrir un archivo para escritura
    ofstream archivo;
    archivo.open("ejemplo.txt");
    // Saber si un archivo está abierto
    cout << boolalpha << archivo.is_open() << endl;  // true
    archivo << "Contenido del archivo\n";
    archivo.close();

    // Abrir un arhivo para lectura
    ifstream archivo2 ("ejemplo.txt");
    string linea;
    if (archivo2.is_open()) {   // Leer las líneas de un archivo
        while ( getline(archivo2, linea) ) {
            cout << linea << "\n";
        }
        archivo2.close();
    } else { cout << "Imposible abrir el archivo\n"; }

    return 0;
}

/* Fuentes:
http://www.cplusplus.com/doc/tutorial/files/
*/
