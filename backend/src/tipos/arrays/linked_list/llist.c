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

La ventaja principal de las listas enlazadas sobre los arrays es que permiten
    aumentar y reducir su tamaño en tiempo de ejecución. No se necesita conocer
    su tamaño máximo por adelantado. En aplicaciones prácticas, esto permite a
    menudo tener varias estructuras de datos compartiendo el mismo espacio sin
    tener que poner atención en su tamaño relativo.
Otra ventaja es que proporcionan flexibilidad al permitir reordenar los elementos
    de forma eficiente. Esta flexibilidad se gana a costa del acceso rápido a
    elementos arbitrarios de la lista.
*/

// Creamos la estructura de datos para los nodos
struct nodo {
    int key;            // Clave numérica (podría ser otra cosa)
    struct nodo* next;  // Puntero al próximo nodo
};

// Inicialización de las funciones
struct nodo* crear_nodo(int new_key, struct nodo* new_next);
void eliminar_nodo(struct nodo *n);


int main() {

    // Definimos el nodo de cabecero y el de cola
    struct nodo *cabecero, *Z;
    struct nodo *n1, *n2; // Lista enlazada

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
    cabecero->next = n1;  // Primer nodo de la lista
    n2 = crear_nodo(2, n1);

    // Acceder a los elementos de la lista enlazada
    printf("La clave del primer elemento en la lista es %d\n",
    	   cabecero->next->key);

    // Eliminamos nodos
    eliminar_nodo(n1);
    eliminar_nodo(n2);

    return 0;
}

/**
 * Crea un nuevo nodo
 * @param  new_key  Clave
 * @param  new_next Nodo de enlace
 * @return          Nuevo nodo creado
 */
struct nodo* crear_nodo(int new_key, struct nodo* new_next) {
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