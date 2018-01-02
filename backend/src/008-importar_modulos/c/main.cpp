#include <iostream>
using namespace std;

int main(){
    // INCLUIR DEL MISMO DIRECTORIO
    #include "modulo.cpp"    // cout << "Desde otro fichero en "
    #include "modulo2.cpp"   // "el mismo directorio" << endl;
    
    // INCLUIR DESDE OTRO DIRECTORIO
    #include "directorio/modulo.cpp"
    
    return 0;
}

/* Fuente:
https://trucosinformaticos.wordpress.com/2012/10/14/como-usar-include-en-c-y-c/
*/
