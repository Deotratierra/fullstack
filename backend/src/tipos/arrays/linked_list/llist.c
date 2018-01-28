#include <stdio.h>
#include <stdlib.h>  // malloc()

/*                        LISTAS ENLAZADAS

Una lista enlazada es un conjunto de elementos organizados secuencialmente,
    como un array. En un array, la organización secuencial es provista de forma
    implícita (por la posición en memoria de los elementos, uno tras otro).
    En una lista enlazada se usa una forma de ordenación explícita en la cual
    cada elemento es parte de un nodo que contiene un enlace al nodo siguiente.
Debido a que todos los elementos deben tener un enlace a un nodo, el último nodo
    será un nodo maniquí que apuntará a sí mismo (lo llamaremos Z). De la misma
    forma, tendremos un nodo al principio de la lista que también será un maniquí
    y apuntará al primer nodo, para determinar que tal nodo es el primero
    (lo llamaremos CABECERO). Tendríamos algo así:

    CABECERO ─> 1 ─> 2 ─> 3 ─> Z <─┐
                               └───┘
Pero también podría ser:
                ┌─────────┐    ┌───┐
    CABECERO ─> 1 ┌─ 2    3    Z <─┘
                  │  └────┘    │
                  └────────────┘

Las reglas para los nodos de cabeza y cola son arbitrarias y pueden cambiarse
    dependiendo del tipo de implementación que necesitemos. Por ejemplo,
    podríamos definir que el nodo Z apuntara a NULL o que apuntara al nodo
    de cabeza para tener una lista circular.
Otra variante de esta implementación simple podrín ser una lista doblemente
    enlazada, en las cual cada nodo tendría un campo anterior y otro siguiente
    y podría ser recorrida en ambas direcciones.

---------------------------------------------------------------------------

                                 VENTAJAS

La ventaja principal de las listas enlazadas sobre los arrays es que permiten
    aumentar y reducir su tamaño en tiempo de ejecución. No se necesita conocer
    su tamaño máximo por adelantado. En aplicaciones prácticas, esto permite a
    menudo tener varias estructuras de datos compartiendo el mismo espacio sin
    tener que poner atención en su tamaño relativo.
Otra ventaja es que proporcionan flexibilidad al permitir reordenar los elementos
    de forma eficiente. Esta flexibilidad se gana a costa del acceso rápido a
    elementos arbitrarios de la lista.

===============================================================================
*/

// Creamos la estructura de datos para los nodos
struct nodo {
    int key;            // Clave numérica (podría ser otra cosa)
    struct nodo* next;  // Puntero al próximo nodo
};

// Inicialización de las funciones
struct nodo *crear_nodo(int new_key, struct nodo* new_next);
void eliminar_nodo(struct nodo *n);
struct nodo *buscar_nodo(struct nodo* cabecero, struct nodo* n);
void insertar_nodo_al_principio(struct nodo* n, struct nodo* cabecero);
void insertar_nodo_al_final(struct nodo* n, struct nodo* cabecero);


int main() {

    // Definimos el nodo de cabecero y el de cola
    struct nodo *cabecero, *Z;
    struct nodo *n1, *n2, *n3; // Lista enlazada

    // Asignamos memoria a los nodos "maniquí"
    cabecero = (struct nodo*) malloc(sizeof(*cabecero));
    Z = (struct nodo*) malloc(sizeof(*Z));

    // Enlazamos el cabecero con el final y el final con sí mismo
    cabecero->next = Z;
    Z->next = Z;

    cabecero->key = 0;  // La clave del cabecero es 0
    Z->key = -1;        // y la clave de la cola es -1

    // Creamos nodos
    n1 = crear_nodo(1, Z);
    n2 = crear_nodo(2, Z); // Los vamos insertando uno tras otro
    insertar_nodo_al_final(n2, cabecero);
    n3 = crear_nodo(3, Z);
    insertar_nodo_al_final(n3, cabecero);


    // Acceder a los elementos de la lista enlazada
    printf("La clave del primer elemento en la lista es %d\n",
    	   cabecero->next->key);

    char* encontrado;
    if (buscar_nodo(cabecero, n2) == NULL) {
        encontrado = "no";
    } else {
        encontrado = "si";
    }
    printf("El nodo de clave %d %s se encuentra en la lista.\n",
           n2->key, encontrado);


    // Eliminamos nodos
    eliminar_nodo(n1);
    eliminar_nodo(n2);
    eliminar_nodo(n3);

    return 0;
}

// =========================================================================
//                             FUNCIONES

/**
 * Crea un nuevo nodo
 * @param  new_key  Clave
 * @param  new_next Nodo de enlace
 * @return          Nuevo nodo creado
 */
struct nodo *crear_nodo(int new_key, struct nodo* new_next) {
    struct nodo* nuevo;     // Creamos un nuevo nodo,
    nuevo = (struct nodo*) malloc(sizeof(*nuevo)); // le asignamos memoria,
    nuevo->key = new_key;   // la nueva clave
    nuevo->next = new_next; // y el nuevo enlace pasado como argumento

    printf("Nuevo nodo creado correctamente:\n\tClave = %d\n\tEnlace = %d\n",
    	   nuevo->key, nuevo->next->key);

    return nuevo;
}

/**
 * Elimina un nodo de la lista enlazada
 * @param n  Nodo a eliminar de la lista
 */
void eliminar_nodo(struct nodo *n) {
    printf("El nodo %d fue eliminado correctamente.\n", n->key);
    printf("El enlace al nodo %d podría haber quedado roto.\n", n->key);

    free(n);
    n = NULL;
}

/**
 * Comprueba si un nodo pasado como argumento
 *   existe dentro de la lista
 * @param  cabecero  Nodo cabecero de la lista
 * @param  n         Nodo a buscar
 * @return           Devuelve el nodo si se encuentra,
 *                     si no, devuelve NULL
 */
struct nodo *buscar_nodo(struct nodo* cabecero, struct nodo* n) {
    struct nodo *actual = cabecero;
    while (actual->next != actual) {
        actual = actual->next;  // Vamos iterando por todos los nodos
        if (actual == n) {
            return n;
        }
    }
    return NULL;
}

/**
 * Inserta un nodo al principio de la lista,
 *   haciendo que el cabecero apunte al nodo
 *   pasado como argumento. Comprueba que el nodo
 *   ca
 * @param  cabecero Nodo cabecero de la lista
 * @param  n        Nodo a insertar al principio
 */
void insertar_nodo_al_principio(struct nodo* cabecero, struct nodo* n) {
    n->next = cabecero->next->next;
    cabecero->next = n;
}

/**
 * Inserta un nodo al final de la lista
 * @param cabecero Nodo cabecero de la lista
 * @param n        Nodo a insertar
 */
void insertar_nodo_al_final(struct nodo* cabecero, struct nodo* n) {
    struct nodo *actual = cabecero;
    while (actual->next != actual) {
        if (actual->next == actual->next->next) { // Si próximo y siguiente coinciden
            actual->next = n;       // El próximo será el nodo a insertar
            n->next = actual->next; // El siguiente al insertado será el próximo
            break;
        } else {
            actual = actual->next;
        }
    }
}


// ============================================================================

/* Fuentes:
Algoritmos en C - Robert Sedgewick
Programación en C, Metodología, Algoritmos y estructuras de datos -
    Luis Joyannes Aguilar e Ignacio Zahonero Martínez
*/
