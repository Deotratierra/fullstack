#include <stdio.h>
#include <stdlib.h>

/* En el siguiente ejemplo se implementa una pila de números enteros: */

// Definición de tipos
typedef unsigned long ulong;

// Definición de estructuras de datos
struct node {
    ulong value;
    ulong *next;
};

struct stack {
    long n_elems;
    long max_elems;
    struct node* top;
};

// Inicialización de funciones
void show_stack(struct stack *_s);
struct stack* create_stack(long _max_elems);
struct node* push(struct stack *_s, long _value);
struct node* pop(struct stack *_s);
char empty(struct stack *_s);
struct node* peek(struct stack *_s);
long poke(struct stack *_s, long _new_value);

int main() {
    // Creación de una pila
    struct stack *pila1;
    // Si creamos una pila con 0 elementos salta un error:
    //pila1 = create_stack(0);
    pila1 = create_stack(4);

    // Comprobar si está vacía
    if (empty(pila1) == 1) {
        printf("La pila está vacía.\n");
    } else {
        printf("La pila no está vacía.\n");
    }

    // Insertamos elementos
    struct node *n;
    int cont = 500;
    for (int i=0; i<5; i++) {
        n = push(pila1, cont); // Insertar un elemento
        if (n == NULL) {  // Comprobar si se insertó el valor (si no está llena)
            printf("No se pudo insertar el valor %d.\n", cont);
        } else {
            show_stack(pila1);  // Mostrar la pila
        }
        cont = cont-100;
    }

    // Sacar el elemento tope de la pila
    n = pop(pila1);
    if (n != NULL) {
        printf("El elemento %d fue sacado de la pila.\n", n->value);
        show_stack(pila1);
    }

    // Obtener el elemento tope de la pila sin sacarlo
    n = peek(pila1);
    if (n != NULL) {
        printf("El valor del elemento tope de la pila es %d\n", n->value);
        show_stack(pila1);
    }

    return 0;
}

/**
 * Muestra los datos de una pila
 * @param _s Pila a mostrar
 */
void show_stack(struct stack *_s) {
    printf("struct stack {\n\tn_elems = %d\n\tmax_elems = %d\n",
           _s->n_elems, _s->max_elems);
    if (_s->top != NULL) {
        printf("\tnode* top->value = %d\n", _s->top->value);
    }
    printf("};\n");
}

/**
 * Asigna memoria para una pila y la inicializa
 * @param  _max_elems Número máximo de elementos en la pila
 * @return            Puntero a la dirección de memoria de la pila
 */
struct stack* create_stack(long _max_elems) {
    if (_max_elems == 0) {
        printf("ERROR: La pila debe tener más de 0 elementos.\n");
        exit(1);
    }
    struct stack* new_s = malloc(sizeof(struct stack));
    new_s->n_elems = 0;
    new_s->max_elems = _max_elems;
    new_s->top = NULL;
    return new_s;
}

/**
 * Inserta un elemento en la pila
 * @param  _s     Pila donde insertar el elemento
 * @param  _value Valor a insertar
 * @return        Si la pila está llena devuelve NULL,
 *                  si no devuelve un puntero al nodo insertado
 */
struct node* push(struct stack *_s, long _value) {
    if (_s->n_elems == _s->max_elems) {
        printf("ERROR: La pila está llena.\n");
        return NULL;
    } else {  // Si hay espacio en la pila
        struct node* new_n = malloc(sizeof(struct node)); // Crea un nuevo nodo
        new_n->value = _value;
        if (_s->top == NULL) {     // Si es el primer elemento en la pila
            new_n->next = NULL;    // no hay siguiente elemento...
        } else {                   // ...pero si ya existen elementos
            new_n->next = _s->top; // el siguiente será el último en el tope
        }
        _s->top = new_n;
        _s->n_elems++;
        return new_n;
    }
}

/**
 * Saca el elemento en el tope de la pila
 * @param  _s Pila de donde sacar el elemento
 * @return    Puntero al elemento sacado
 */
struct node* pop(struct stack *_s) {
    if (_s->n_elems == 0) {
        printf("ERROR: La pila está vacía.\n");
        return NULL;
    } else {
        struct node *temp;
        temp = _s->top;
        if (_s->n_elems == 1) {  // Si es el último elemento en la pila
            _s->top = NULL;      // el próximo elemento será NULL...
        } else {                 // ...pero si no es el último en la pila
            _s->top = _s->top->next; // el siguiente será el siguiente al tope
        }
        _s->n_elems--;
        return temp;
    }
}

/**
 * Comprueba si una pila está vacía
 * @param  _s Pila a comprobar
 * @return    Devuelve 1 si está vacía, 0 si está llena.
 */
char empty(struct stack *_s) {
    if (_s->n_elems == 0) {
        return 1;
    } else {
        return 0;
    }
}

/**
 * Obtiene el elemento tope de la pila sin eliminarlo
 * @param  _s Pila de donde obtener el elemento
 * @return    Puntero al elemento obtenido
 */
struct node* peek(struct stack *_s) {
    if (_s->n_elems == 0) {
        printf("ERROR: La pila está vacía.\n");
        return NULL;
    } else {
        return _s->top;
    }
}
