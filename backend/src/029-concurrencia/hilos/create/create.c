#include <stdio.h>

// ===================================================================================

//                                HILOS (GENERAL)

/* Los hilos son unidades de ejecución más finas que los procesos. Cuando
    invocas un pograma, Linux crea un nuevo proceso y en dicho proceso crea
    un solo hilo, el cual corre el programa secuencialmente. Ese hilo puede
    crear hilos adicionales: todos esos hilos corren el mismo programa en el mismo
    proceso, pero cada hilo puede estar ejecutando una parte diferente del programa.

A diferencia de los procesos, cuando un programa crea otro hilo, no se copia nada
    del hilo creador. El hilo creador y el creado comparten el mismo espacio de memoria,
    los mismos descriptores de archivo y otros recursos del sistema. Si un hilo cambia
    el valor de una variable, por ejemplo, el otro hilo también será modificado.
Por esto, al trabajar con datos compartidos entre dos o más hilos, debe usarse
    un sistema de sincronización como los semáforos.
*/


// ===================================================================================

/*                                     UNIX
Compilación:
gcc create.c -o create -lpthread
*/
#ifdef __unix__

#include <pthread.h>
#include <unistd.h>      // usleep(), SYS_gettid
#include <sys/syscall.h> // gettid()

/*
GNU/Linux implementa la API según el estándar POSIX conocida como pthreads. Todas las
    funciones y los tipos de datos de esta se encuentran en el cabecero <pthread.h>.
    y la biblioteca dinámica puede ser hallada buscando:
    locate libpthread.so
Para compilar programas que usen esta biblioteca debe ser enlazada con:
    -lpthread

Debido a que un proceso y todos sus hilos pueden ejecutar un programa al mismo tiempo,
    si algún hilo dentro de un proceso llama a alguna de las funciones exec, todos
    los otros hilos en ejcución dentro del proceso serán terminados.
*/

void* hola(void* parametro);

int main() {
    /* Cada hilo en u proceso está identifiaco por su identificador. Para referirnos
    a los identificadores de los hilos usamos el tipo de dato pthread_t */
    pthread_t hilo_ID;

    /* Al momento de crearse, cada hilo ejecuta una función. Cuando esta retorna,
        el hilo termina. En Linux, las funciones de hilos toman un sólo parámetro de
        tipo void* (podemos usar este parámetro para mandar información al nuevo hilo)
        y retornan un argumento del mismo tipo (de forma similar mandamos información
        de vuelta).

    La función pthread_create() crea un nuevo hilo y podemos pasarle 4 argumentos:
        1. Un puntero a una variable pthread_t, en la cual se alamecena el identificador
            del nuevo hilo.
        2. Un puntero a un atributo de un objeto thread. Este objeto controla detalles
            sobre como el hilo interactúa con el resto del programa. Si pasas NULL
            como atributo del objeto, el hilo será creado con los atributos por defecto.
        3. Un puntero a la función que ejecutará el hilo. Este es un puntero a una función
            normal, de este tipo: void* (*) (void*).
        4. Un argumento de tipo void* para pasarlo al hilo. Lo que introduzcas simplemente
            se pasa como argumento a la función que el hilo ejecutará.
    */
    int parametro = 1;
    pthread_create(
        &hilo_ID,          // Identificador del hilo
        NULL,              // Atributos de creación
        &hola,             // Función a ejecutar
        (void*)&parametro // Parámetro a pasar a la función (casting de int a void*)
    );

    // Dormimos un momento el hilo principal para ver el parámetro pasado al hilo
    usleep(2000000);

    // Imprime ceros sin parar
    while (1) { printf("%d", 0); }  // Imprime ceros

    return 0;
}
/**
 * Función que imprime unos sin parar.
 * @param sin_uso Variable necesaria por la función pero no usada.
 */
void* hola(void* parametro) {
    int i = (*(int *) parametro);  // Casting de void* a int
    printf("Parámetro pasado al hilo: %d\n", i);

    // Obtener su número identificador dentro del hilo:
    #ifdef SYS_gettid
    pid_t tid = syscall(SYS_gettid);
    printf("Identificador del hilo: %d\n", tid);
    #else
    #error "SYS_gettid unavailable on this system"
    #endif

    usleep(3000000);

    while (1) { printf("%d", i); }  // Imprime unos
    return NULL;
}

/* __unix__ */

// ===================================================================================

/*                                  WINDOWS
Compilación:
gcc create.c -o create
*/
#elif defined(_WIN32)
#include <windows.h>

/* Cada hilo en Windows posee los siguientes atributos:

    - Un número único de 32 bits asociado que funciona como identificador.
    - El estado de los registros del procesador
    - Una pila (stack)
    - Parámetros de seguridad Session ID y Security Descriptor. El identificador
        de sesión identifica al usuario ejecutando el hilo. El descriptor de seguridad
        identifica a los permisos del hilo dentro del sistema operativo. Por defecto
        coinciden con los del hilo principal del proceso.
    - Un valor de prioridad, que por defecto es el mismo que el del hilo principal.
    - Una entrada en la lista de ejecuciones de Windows.
    - Opcionalmente, una cola de mensajes.
*/

DWORD WINAPI hola(LPVOID parametro);

int main() {
    DWORD hilo_ID, parametro = 1;
    HANDLE manejador_de_hilo;

    /* Para crear un hilo usamos la función CreateThread(). A diferencia de Linux,
        la función para crear hilos devuelve un manejador del hilo desde el cual
        se ejecutan las funciones que afectan al hilo. Este manejador hay que
        cerrarlo cuando ya no se use. Puede ser utilizado, entre otras cosas,
        para conocer el estado del hilo. */

    manejador_de_hilo = CreateThread(
        NULL,       // Atributos de seguridad (los del hilo actual con NULL)
        0,          // Tamaño de pila (por defecto con 0)
        hola,       // Función a ejecutar por el hilo
        &parametro, // Argumento a pasar a la función del hilo
        0,          // Banderas de creación del hilo (por defecto con 0)
        &hilo_ID    // Almacenar el identificador del hilo
    );

    printf("Identificador del hilo: %d.\n", hilo_ID);

    // Comprueba el valor de retorno
    if (manejador_de_hilo == NULL) {
        printf("Ocurrió un error en la función CreateThread(): %d.\n", GetLastError());
    } else {
        printf("Hilo creado correctamente.\n");
    }

    // Cerramos siempre el manejador del hilo cuando no lo necesitamos
    // (esta acción no afectará a la ejecución del hilo)
    if (CloseHandle(manejador_de_hilo) != 0) {
        printf("Manejador de hilo cerrado con éxito.\n");
    } else {
        printf("Ocurrió un error cerrando el manejador de hilo.\n");
    }

    // Dormimos un momento el hilo principal para ver el parámetro pasado al hilo
    Sleep(2000);

    while (1) { printf("%d", 0); }  // Imprime ceros

    return 0;

}

/**
 * Función a ejecutar por el hilo.
 * @param  parametro Parámetro de ejemplo pasado al hilo.
 * @return       Retorna 0 si no sucede ningún error.
 */
DWORD WINAPI hola(LPVOID parametro) {
    int i =  *(DWORD*)parametro;  // Casting de void* a int
    printf("Parámetro pasado al hilo: %u.\n", i);

    Sleep(3000);

    while (1) { printf("%d", i); }  // Imprime unos
    return 0;
}

#endif  /* _WIN32 */

// ===================================================================================

/* Fuentes:
LINUX
Programación avanzada en Linux - Mark Mitchell, Jeffrey Oldham y Alex Samuel
https://stackoverflow.com/questions/5153096/pthread-library-location

WINDOWS:
http://7542.fi.uba.ar/tecnica/windows-y-los-threads/
http://www.tenouk.com/cpluscodesnippet/createathread.html
*/
