#include <iostream>
#include <array>
#include <vector>
#include <set>

using namespace std;

/*Es posible que nos de fallos al compilarlo. Estos se solucionan
  agregando la opción -std=c++11 al compilar. Por ejemplo, este archivo
  se compilaría con la siguiente instrucción:

  g++ arrays.cpp -std=c++11 -o arrays
/*

/* En C++, hay varias formas de crear arrays y cada una posee
diferentes características: */

int main(){
    // =================================================================

    // #####   Array básico desde 0   #####
    cout << "\n#####     Array básico desde 0     #####\n" << endl;

    // -------------------------------------------------------

    // INICIALIZACIÓN

    int lista1[5];    // Array de 5 enteros
                    // (al ser un array de enteros, se inicializa con ceros)
    int lista2[5] = {}; // Igual que lista1
    int lista3[] = {1, 2, 3, 4, 5}; // Será un array de 5 enteros
    int lista4[5] = {1, 2, 3, 4, 5};
    int lista5[5] = {1, 2, 3}; // Los valores no aportados (lista5[3] y lista5[4])
                               // son inicializados con ceros
    int lista6[5] {1, 2, 3, 4, 5}; // El signo = es opcional

    string lista7[] = {"hola", "que tal"}; // Array de 2 strings

    // ---------------------------------------------------------

    // ACCESO A SUS VALORES

    cout << lista6[4] << endl;  // 5
    cout << lista7[1] << endl; // que tal
    lista7[1] = "muy bien";           // <-- Modificación de un elemento
    cout << lista7[1] << endl; // muy bien

    for (int n=0; n<5; ++n){
        cout << lista5[n] << " ";  // 1 2 3 0 0
    }
    cout << "\n";

    //cout << lista5.size(); // No podemos obtener su tamaño

    cout << "=================================================" << endl;
    // =================================================================

    // #####     std::array     #####
    cout << "\n#####     std::array     #####\n" << endl;

    /* Es la version en forma de clase del array clásico de C.
    Esto siginifica que su tamaño se fija en tiempo de compilación
    y será asignado como un sólo pedazo en la memoria.
    La ventaja que tienes es que es ligeramente más rápido que
    un vector, debido a que no hay indirección entre el objeto
    y la información que contiene.

    Ocupa algo más de memoria que el array básico pero es más
    fácil de utilizar, debido a que podemos acceder a su información
    mediante ciertas funciones.
    http://es.cppreference.com/w/cpp/container/array

    Realmente es un contenedor de tipos,
    incluido en la biblioteca estándar de C. Para utilizarlo
    hay que importarlo:

    #include <array>

    */

    // -------------------------------------------------------

    // INICIALIZACIÓN

    array<double, 3> lista8 = {3.14, 1.75, 9.99};
    array<string, 2> lista9 = {"hola otra vez", "que tal de nuevo"};
    array<int, 10> lista10;

    // -------------------------------------------------

    // ACCESO A SUS VALORES

    cout << lista9.size() << endl; // Podemos acceder a su tamaño
    cout << lista10.max_size() << endl; // Número máximo de elementos

    for (int n = 0; n < lista8.size(); ++n){
        cout << lista8[n] << endl;
    }

    cout << lista9.back() << endl; // Último elemento --> que tal de nuevo

    // Iterador
    /* Existen unas funciones especiales sobre los contenedores
    para iterar sobre ellos.

    Para iterar por un array podemos usar las funciones begin(),
    que hace referencia al primer elemento del array, y end(),
    que referencia al último. El especificador auto indica que
    el tipo de la variable p será deducida del primer elemento.
    Accedemos al valor de cada elemento con un puntero a p (*p).
    */
    for (auto p = lista8.begin(); p != lista8.end(); ++p){
        cout << *p << " ";      // 3.14 1.75 9.99
    }
    cout << "\n";

    cout << "=================================================" << endl;
    // =================================================================

    // #####     std::vector     #####
    cout << "\n#####     std::vector     #####\n" << endl;

    /* Es una pequeña clase contenedora de punteros en su interior,
    (así que cuando asignas a std::vector, siempre llama a new).

    Son ligeramente más lentos de acceder debido a que sus punteros
    tienen que ser perseguidos para obtener la información que contienen...
    pero, en cambio, pueden ser redimensionados y sólo toman un poco de
    espacio de memoria, no importa lo largo que sean.

    http://es.cppreference.com/w/cpp/container/vector

    Son el tipo de objetos más parecidos a una lista en Python,
    pero difieren en algunas cosas, por ejemplo, no puedes insertar
    elementos de distinto tipo.

    Para usarlos hay que importarlos de la biblioteca estándar:
    #include <vector>
    */

    // -------------------------------------------------------

    // INICIALIZACIÓN

    vector<string> lista11 = {"primero", "segundo", "tercero"};
    vector<int> lista12 = {1, 2, 3};
    vector<int> lista13; // Vector sin capacidad reservada
    vector<int> lista14(5); // Vector de 5 elementos inicializado a 0

    // -------------------------------------------------------

    // ACCESO A SUS ELEMENTOS

    cout << lista11[0] << endl;  // primero
    cout << lista12[1] << endl;  // 2

    cout << lista12.front() << endl;  // Primer elemento --> 1
    cout << lista11.back() << endl;  // Último elemento --> tercero

    // Intento de acceso a un elemento de un índice inexistente:
    try{
        lista14.at(100) = 0; // at(100) coge el elemento en la posición 100
    }                        // Salta un error  --->  std::out_of_range
    catch(std::out_of_range o){
        cout << o.what() << endl; // what() Retorna un string relacionado
    }                             //        con la excepción

    // Agregar y eliminar elementos
    lista11.push_back("cuarto"); // Agrega elementos al final
    cout << lista11[3] << endl;  // cuarto
    lista11.pop_back(); // Elimina el último elemento
    cout << lista11[3] << endl; //        (Vacío)

    lista11.clear(); // Elimina todos los elementos

    cout << "=================================================" << endl;
    // =================================================================

    // #####     std::set     #####
    cout << "\n#####     std::set     #####\n" << endl;

    /* http://www.cplusplus.com/reference/set/set/

    Los sets (conjuntos) son contenedores que almacenan elementos
    únicos siguiendo un orden específico.
    En un set, el valor de un elemento también lo identifica.
    El valor de los elementos de un set no pueden ser modificados
    una vez que se encuentran en el contenedor, pero pueden
    ser insertados y removidos del mismo.

    Para usar los sets, hay que importarlos de la biblioteca estándar:
    #include <set>
    */

    // -------------------------------------------------------

    // INICIALIZACIÓN

    set<char> lista15;
    set<int> lista16 = {1, 2, 3};

    // -------------------------------------------------------

    // ACCESO A SUS ELEMENTOS

    // Contar el número de elementos de un valor (1 ó 0)

    cout << lista16.count(3) << endl;  // 1
    cout << lista15.count(1) << endl;  // 0

    // Buscar si existe un elemento
    if (lista16.count(2) > 0){
        cout << "El número 2 existe en el set" << endl;
    } else {
        cout << "El número 2 no existe en el set" << endl;
    }

    if (lista16.find(4) != lista16.end()) {
        cout << "El número 4 existe en el set." << endl;
    } else {
        cout << "El número 4 no existe en el set." << endl;
    };

    cout << lista16.size() << endl;  // 3  <--- Cantidad de elementos
    cout << lista15.empty() << endl;  // 1  <--- Comprobar si está vacío

    // -------------------------------------------------------

    // MODIFICACIÓN

    // Insertar elementos
    lista15.insert(75); lista15.insert(75); // Sólo uno es válido
    cout << lista15.count(75) << endl; // 1

    // Eliminar elementos
    lista16.erase(2);
    cout << lista16.count(2) << endl; // 0

    cout << "=================================================" << endl;
    // =================================================================

    return 0;
}

// #####     Consideraciones sobre uso en cada caso     #####

/*
std :: vector es casi siempre lo que necesitamos.
Crear grandes objetos en la pila está, generalmete, mal visto,
y el nivel adicional de indirección suele ser irrelevante.
Por ejemplo, si itera a través de todos los elementos, el acceso
a la memoria adicional solo se produce una vez al inicio del ciclo).

Dicho esto, la falta de ese nivel extra de indirección,
más el tamaño constante en tiempo de compilación,
pueden hacer que std::array sea significativamente más rápido
para un array muy pequeño que se crea / destruye / accede mucho.

Usar std::vector a menos que (a) su generador de perfiles
le diga que tiene un problema o (b) que el array sea pequeño.
*/


/* Fuentes:
* http://www.cplusplus.com/doc/tutorial/arrays/
* https://stackoverflow.com/questions/6632971/what-is-the-difference-between-stdarray-and-stdvector-when-do-you-use-one-o
* https://stackoverflow.com/questions/25594019/array-is-not-a-member-of-std
* https://trucosinformaticos.wordpress.com/tag/array-multidimensional/
* http://en.cppreference.com/w/cpp/language/auto
* http://www.cplusplus.com/reference/exception/exception/what/
* http://www.cplusplus.com/reference/set/set/
*/
