#include <stdio.h>

// Siempre que trabajamos con memoria es importante incluir la biblioteca
#include <stdlib.h>  // ya que al realizar conversiones de tipos de punteros
// a memoria, si no la incluimos el comportamiento puede quedar indefinido


//     GESTION DE MEMORIA EN C  //
//  -----------------------  //

int main() {
    //  TIPOS DE MEMORIA  //
    /* Un programa en C almacena sus datos en memoria en 3 áreas diferentes:
      1. Memoria global: es el área donde se declaran las variables globales
          y las cadenas de caracteres. Esta es la única área que tiene un tamaño
          fijo ya definido al inicio de la ejecución del programa.
      2. Pila: área utilizada para almacenar variables locales a las funciones.
      3. Montón (heap): contiene memoria disponible para reservar y liberar
          a conveniencia durante la ejecución del programa. Guarda estructuras
          de datos que no sabe si se necesitan o su tamaño hasta la ejecución.
    */

    // ========================================================================

    //  GESTIÓN DE MEMORIA  //
    /* Se realiza mediante dos operaciones básicas, la petición y la liberación
      de memoria. Las 4 operaciones para gestionar memoria en C son: */

    //         ---------------------------------------------------------------

    //  malloc
    void *malloc(size_t, size);  /* Es la función para reservar tantos bytes
      consecutivos de memoria como indica su único parámetro. La memoria no
      se inicializa a ningún valor.

      Devuelve la dirección de memoria de la porción reservada, pero por medio
      de un puntero que no apunta a un tipo de datos determinado, es decir
      de tipo *void. Para convertirlo a otro tipo de puntero (casting): */
    char* ptr = (char*)malloc(500);  // con (char*) indicamos el cambio de tipo

    /* El problema del ejemplo anterior es que no sabemos cuantos bytes ocupa
      el tipo char, por lo que podemos reescribirlo usando la función sizeof(),
      que nos devuelve el número de bytes que ocupa un tipo: */
    char* ptr = (char*)malloc(sizeof(char));

    /* Si no existe espacio de memoria para conceder el bloque,
      devolverá un puntero nulo: */
    int *i;
    i = malloc(sizeof(int));
      // Verificar que la asignación ha sido llevada a cabo correctamente:
    if (i == NULL) {
        printf("Error al intentar reservar memoria.")
    }

    // --------------------------------------------------------------------------

    //  free
    void free(void *ptr);  /* Dado un puntero obtenido con una llamada de reserva
      de memoria, libera dicho espacio de memoria reservado. Una vez ejecutada la
      llamada, los datos en esa porción de memoria se consideran basura y pueden
      ser reutilizados por el sistema.

    Para liberar el espacio del ejemplo reservado con malloc(): */
    free(ptr);

    /* Si el puntero es nulo free() no hace nada. Si se libera dos veces el mismo
      espacio de memoria, puede ser desastroso. Por lo tanto, es conveniente
      siempre establecer el valor de un puntero a NULL para evitarnos problemas: */
    ptr = NULL;
    free(ptr); // Ya no pasa nada si volvemos a liberar el mismo espacio por error

    // --------------------------------------------------------------------------

    //  calloc
    void *calloc(size_t n_members, size_t size);  /* Reserva espacio para tantos
    elementos como indica su primer parámetro y cada uno de ellos con el número de
    bytes como indica el segundo, es decir, reserva n_members * size bytes
    consecutivos de memoria. Al igual que malloc(), devuelve la dirección de memoria
    al comienzo del bloque reservado. Inicialia todos los bytes de la zona reservada
    al valor 0. */

    // ---------------------------------------------------------------------------

    // realloc()
    void *realloc(void *ptr, size_t size);  /* Redimensiona una porción de memoria
    previamente reservada a la que apunta el primer parámetro al tamaño pasado
    como segundo argumento. Devuelve la dirección de memoria de esta nueva porción
    redimensionada, que no tiene por que ser la misma a la que se ha pasado como
    primer parámetro. Los datos se conservan intactos en tantos bytes como el mínimo
    entre el tamaño antiguo y el nuevo. */

    // =======================================================================

    //  APLICACIONES  //

    /* Uno de los usos más comunes es la creación de vectores con un número de
    elementos definido en tiempo de ejecución: */

    //  malloc()
    int *vector1, n1;
    printf("Número de elementos del vector: ");
    scanf("%d", &n1);

    vector1 = malloc(n1 * sizeof(int));
    if (vector1 == NULL) {
        printf("Error al intentar reservar memoria.");
    }

    // --------------------------------------------------------------------------

    //  calloc()
    int *vector2, n2;
    printf("Número de elementos del vector: ");
    scanf("%d", &n2);

    vector2 = calloc(n2, sizeof(int));
    if (vector2 == NULL) {
        printf("Error al intentar reservar memoria.");
    }

    // ======================================================================

    //  FUGA DE MEMORIA  //

    /* Esta situación ocurre cuando un programa tiene memoria dinámica y el valor
      del puntero se pierde por error. En tal caso, ya no se puede invocar a free()
      con ese puntero y la porción de memoria se queda reservada por lo que resta
      de ejecución: */
    char *cadena;
    cadena = (char *)malloc(100);
    cadena = NULL;
    /* Dado que cadena es la única copia de la dirección de memoria reservada,
      tras establecer su variable a NULL ya no hay manera de recuperarla.
      La memoria "se ha fugado" */

    // =======================================================================

    /*                        PREGUNTAS COMUNES
    1. ¿Qué pasa si asigno memoria para mi variable y no llamo a free() antes
        de cerrar el programa?
      En los sistemas operativos modernos no pasa nada porque el propio sistema
          se encargará de recoger toda esa memoria. Piénsalo un momento: realmente
          tendrías que desasignar memoria para cada variable que declararas y antes
          de cada salida del programa con exit() o return tendrías que ponerte a
          llamar a free() una y otra vez. Esto no hace falta, llamar a free() antes
          de cerrar un programa es inútil, el sistema operativo la reclamará de
          todas formas.
    */

    // =======================================================================

    return 0;
}

/* Fuentes:
http://www.it.uc3m.es/abel/as/MMC/M1/MallocFreeExplained_es.html
https://es.wikibooks.org/wiki/Programaci%C3%B3n_en_C/Manejo_din%C3%A1mico_de_memoria
http://sopa.dis.ulpgc.es/fso/cpp/intro_c/introc75.htm
http://www.it.uc3m.es/abel/as/MMC/M3/MemoryLeaks_es.html
https://stackoverflow.com/questions/654754/what-really-happens-when-you-dont-free-after-malloc
*/
