#include <iostream>

using namespace std;

int main(){
    /* Un puntero suele poseer un tamaño de 4 bytesy se debe declarar
    o definir de acuerdo con el tipo del dato al que apunta: */

    char *direccion;

    /* Para acceder al valor depositado en la zona de memoria
       de una variable se usa el operador de indirección (*)
       y para hallar la dirección en memoria de una variable
       se utiliza el operador dirección (&): */

    int i, *p;     // *p es un puntero, no apunta a ninguna dirección
    p = &i;        // ahora p contiene la dirección en memoria de i
    *p = 10;       // accedemos al valor de i y le asignamos 10

    cout << sizeof(*p) << endl;  // 4
    cout << sizeof(&i) << endl;  // 8

    /* Las constantes y las expresiones no tienen dirección, por lo que no
       se les puede aplicar el operador (&). Tampoco se puede cambiar la
       dirección de una variable. Los valores posibles para un puntero son
       las direcciones posibles de memoria, aunque puede tener valor 0 (null) */

    // Las siguientes sentencias levantan errores
    //p = &34;     // Las constantes (en este caso 34) no tienen dirección
    //p = &(i+50); // Las expresiones (en este caso i+50) no tienen dirección
    //&i = p;      // Las direcciones de las variables no pueden cambiar

    /* No se permiten asignaciones directas (sin casting) entre punteros que apuntan
       a distintos tipos de variables. Sin embargo, existe un tipo indefinido
       de punteros (void *) que puede asignarse a cualquier tipo
       de puntero, aunque no se les puede asignar ningún valor: */

    double *q;
    void *r;
    //p = q;   // No se puede asignar un puntero int a uno double
    r = q;
    //p = r;   // ERROR


    cout << endl;
    // ==========================================================================
    // =============     ARITMÉTICA DE PUNTEROS     ================

    /* Se pueden realizar operaciones con los punteros. Ya que estos apuntan a
       una dirección de memoria y guardan el tipo de variable a la que apuntan,
       si sumamos un puntero: */
    p += 1;
    /* p apuntará a la siguiente dirección de memoria teniendo en cuenta el tipo
       de dato */

    cout << sizeof(p) << endl;  // 8
    cout << p << endl;
    p += 1;                     // 8 bytes de diferencia entre ambas direcciones
    cout << p << endl;

    // La misma lógica sucede en los arrays, vectores y cadenas de caracteres


}