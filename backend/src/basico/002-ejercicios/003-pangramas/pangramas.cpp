/* Este programa debe compilarse usando el siguiente comando:
g++ pangramas.cpp -std=c++11 -o pangramas
*/

#include <iostream>
#include <string>
#include <array>
#include <set>

using namespace std;

string abecedario_ingles = "abcdefghijklmnopqrstuvwxyz";

bool pangramas(string str){
    set<char> letras;
    
    for (int n = 0; n < str.size(); n++){
        if ( !isspace(str[n]) ){  // Ignoramos los espacios
            str[n] = char(tolower(str[n])); // Conversión a minúsculas
            // Comprobamos si nuestra letra no está dentro del set
            if ( letras.find(str[n]) == letras.end() ){ 
                // Comprobamos si nuestra letra está en el abecedario
                if ( abecedario_ingles.find(str[n]) < abecedario_ingles.size() ){
                    letras.insert(str[n]);            
                };
            }    
        }
    }
    if ( letras.size() == abecedario_ingles.size() ){
        return true;
    };
    return false;
}


int main(){
    array<string, 4> sentencias = {
        "abcdefGHIJKLMNopqrstuvwxyz",
        "abcdefGHIJKLwNopqrstuvwxyz",
        "Texto de ejemplo",
        "The quick brown fox jumps over the lazy dog"
    };
    
    for (int n = 0; n < sentencias.size(); ++n){
        cout << pangramas(sentencias[n]) << endl;
    }
    
    return 0;    
}

/* Fuentes:
 * http://www.cplusplus.com/reference/cctype/isspace/
 * https://stackoverflow.com/questions/6277646/in-c-check-if-stdvectorstring-contains-a-certain-value
 */
