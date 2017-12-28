#include <iostream>
using namespace std;

int main(){
    char caracter = 'a';
    int caracter_en_ascii = int(caracter);
    cout << "El caracter '" << caracter << "' en ASCII ---> " << caracter_en_ascii << endl;
    
    int numero = 78;    
    char numero_en_caracter = char(numero);
    cout << "El número " << numero << " en en caracter ---> " << numero_en_caracter << endl;
    // Si escribimos un número alto, por ejemplo 434928, nos daría como resultado:
    // El número 7358 en en caracter ---> �
    // Esto es una conversión insegura (la mayoría de los compiladores no la cazan)
    
    return 0;
}
