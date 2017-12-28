#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main() {

    vector<int> nums { 1, 2, 3, 4, 5, 6, 7};
    int x = 4;
    // Por cada número en el vector creamos una función
    // que indicará si es mayor que x
    for_each(nums.begin(), nums.end(), [x](int n) {
        cout << boolalpha << (n > x) << "\n";
    });


    // A la sintaxis [] dentro de la función lambda se le llama
    // cláusula de captura y especifica las variables que serán
    // capturadas del ámbito circundante, como x en el caso anterior.
    cout << "\n";

    // Gracias al cabecero <functional> podemos diseñar al estilo de
    // la programación funcional:
    function<int (int)> func = [](int i) { return i+5; };  // Creamos función
    cout << "func(6): " << func(6) << "\n";       // func(6): 11

	return 0;
}

/* Fuentes:
http://es.cppreference.com/w/cpp/language/lambda
*/