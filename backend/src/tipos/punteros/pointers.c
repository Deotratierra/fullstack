#include <stdio.h>
#include <stdlib.h>  // malloc()

/*                          PUNTEROS EN C

Un puntero es una variable que contiene la dirección de memoria de un dato.
    Para declarar un puntero se coloca * delante de la variable al definirla.
    Para acceder a la dirección de memoria de una variable se coloca &
    delante de ella.
Los punteros pueden apuntar a cualquier tipo de dato y a otros punteros.
    Para que un puntero guarde la dirección de otra variable debe de ser del
    mismo tipo de dato que la variable o del tipo void, que puede apuntar
    a cualquier tipo de dato.
*/

int main() {
    // =========================================================================

    //                     Demostración de comportamiento
    int num = 5;
    int* puntero = NULL;
    puntero = &num;
    printf("El valor de num es: %d\n", num);                      // num = 5
    printf("El valor de *puntero es: %d\n", *puntero);            // *puntero = 5
    printf("La dirección de memoria de *puntero es %p\n", puntero);
    // Con el formateador %p imprimimos la dirección de memoria en hexadecimal

    // ------------------------------------------------------------------------

    //                         Declaración de punteros

    // A cualquier dirección de memoria
    char* hola;     // Puntero que apunta a la variable 'hola' en cualquier dirección de memoria
    hola = "hola";  // Definición de la variable 'hola'
    printf("El saludo es '%s'.\n", hola);

    // Reservando memoria para el puntero
    char* caracter1 = (char*) malloc (sizeof (char));
    scanf (" %c", caracter1);    // Este código y el siguiente son equivalentes

    // Accediendo a la dirección de memoria de una variable
    char caracter2;            // Definimos caracter
    scanf ("%c", &caracter2);  // Pasamos a la función la dirección de memoria del caracter


    // --------------------------------------------------------------------------

    /*                          Punteros a arrays

    Podemos realizar operaciones artiméticas con los punteros. Esto nos permite
        una herramienta perfecta para operar con arrays y sus derivados
        (cadenas de caracteres, matrices...), ya que los elementos de un array
        están almacenados en memoria uno detrás de otro:
    Cuando indicamos a un puntero que apunte a un array, este apuntará a la dirección
        del primer elemento del mismo. Si vamos sumando su dirección podemos avanzar
        por los elementos del array.
    */
    char* saludo;
    saludo = "Buenos días";    // Una cadena de caracteres es un array
    while (*saludo != '\0') {  // El '\0' es el caracter que indica fin de cadena en C
        printf("%c", *saludo); // Imprimimos el valor al que apunta el puntero
        *saludo++;             // Incrementamos el valor del puntero para que apunte
    }                          //     al siguiente elemento en el array
    printf("\n");
    /* En el código anterior se cumple lo siguiente:
        *saludo == saludo[0];
        saludo == &saludo[0];
    */

    // -------------------------------------------------------------------------

    /*                           Punteros a matrices
    Las matrices son arrays dentro de arrays. Llamemos A al array exterior que
        contiene los demás arrays y B a cada uno de los arrays contenidos. Si
        apuntamos con un puntero al primer elemento de A, apuntamos al vector B:
    */
    #define filas 2
    #define columnas 3

    // Definición de matriz
    int A[filas][columnas] = { {1, 2, 3},
                               {4, 5, 6} };

    int* puntero_A = NULL;
    puntero_A = A; // Indicamos que puntero_A apunte a A

    for (int i=0; i<(filas*columnas); i++) {
        printf("*puntero_A = %d\n", puntero_A[0]); // Como apunta al vector cogemos
        puntero_A++;  // el primer elemento de cada uno y vamos incrementando el valor
    }
    printf("\n");

    // El código siguiente es equivalente al anterior:

    puntero_A = A; // Indicamos que puntero_A apunte de nuevo al principio

    for (int i=0; i<(filas*columnas); i++) {
        printf("*puntero_A = %d\n", *puntero_A); // Ahora apuntamos al puntero del
        *puntero_A++;  // puntero, por lo tanto incrementamos el valor del puntero
    }                  // del puntero. Funciona porque los vectores de la matriz
                       // están concatenados en memoria.
    printf("\n");


    // -------------------------------------------------------------------------

    /*                           Punteros a void
    Los punteros void* son un tipo especial de punteros que pueden apuntar a
    cualquier tipo de dato, ya sea int, float, double, etc; también se les
    conoce como "punteros genéricos".
    */

    char* texto = "Un texto";
    int num2 = 33;

    void* ptr;  // Puntero genérico: apuntará a las dos variables anteriores

    ptr = texto; // Apunta a la cadena
    printf("%s\n", (char*) ptr);

    ptr = &num2; // Apunta al número
    printf("%d\n", *(int*) ptr);

    // =========================================================================

    return 0;
}

/* Fuentes:
https://es.wikibooks.org/wiki/Programaci%C3%B3n_en_C/Cadenas_de_caracteres
*/


