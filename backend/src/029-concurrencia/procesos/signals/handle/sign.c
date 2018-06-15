/* La función sigaction() puede ser usada para establecer un comportamiento ante
    una señal. El primer parámetro es el número de señal son punteros a estructuras
    sigaction: la primera contiene la disposición deseada para ese número de señal
    y el segundo recibe la disposición previa.
   El campo más importante en estas estructuras sigaction es sa_handler. Este puede
    tomar uno de los siguientes 3 valores:
        - SIG_DFL: especifica la acción predeterminada.
        - SIG_IGN: ignora la señal.
        - Un puntero a una función manejadora de señal, la cual debe tomar un parámetro
            (el número de la señal) y devolver void.

   Para más información consultar: man sigaction
*/

/* El siguiente programa cuenta las veces que recibe una señal SIGUSR1 */

#include <signal.h>  // Para incluir señales en los programas
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>  // Para obtener los segundos en unix timestamps

// Microsegundos que dormirá el programa para lanzar las señales
int TIEMPO = 30 * 1000000;

/* Asignar un valor a una variable global puede ser peligroso debido a que
    la asignación puede realizarse en dos o más intrucciones del procesador y
    una segunda señal puede llegar entre ambas.
   Si usas una variable global para indicaciones de señales desde una función
    manejadora de señal (como es el caso), debe ser del tipo especial sig_atomic_t.
    Linux garantiza que las asignaciones a variables de este tipo son llevadas a
    cabo en una sola instrucción y por lo tanto no pueden ser interrumpidas. */
sig_atomic_t CONTADOR_SIGUSR1 = 0;

/** Función manejadora de señal
  * @param   signal_number número de la señal recogida por este manejador
  */
void handler(int signal_number) {
    ++CONTADOR_SIGUSR1;
}

int main() {

	char unlock[5];
    int start, end;

    // La variable para la estructura sigaction.
    struct sigaction sa;

    // La función memset establece el la memoria contenido
    // pasando un bloque como primer parámetro, el contenido a insertar en
    // el segundo y el tamaño del bloque a establecer en el tercero:
    // https://www.tutorialspoint.com/c_standard_library/c_function_memset.htm
    memset(&sa, 0, sizeof(sa));

    // Establecemos el manejador
    sa.sa_handler = &handler;

    // Sobreescribimos el comportamiento de la señal en el programa
    sigaction(SIGUSR1, &sa, NULL);
    // El tercero es NULL porque SIGUSR1 no tenía ningún comportaimento asociado


    //  ... añadimos unas instrucciones bloquantes por aquí ...

    printf("Aquí se detiene la ejecución.\nAprovecha para ");
    printf("lanzar unas cuantas señales SIGUSR1 al programa.\nPara ello, ");
    printf("ejecuta kill -SIGUSR1 %d desde otra consola tantas veces como quieras.\n", getpid());
    printf("Tienes %d segundos (%d es el PID del programa).\n", TIEMPO/1000000, getpid());


    /* Debido a que cuando lanzamos una señal la función usleep()
        salta, realizamos el siguiente bucle para poder enviar señales
        durante un tiempo determinado */

    start = (unsigned long)time(NULL);
    end = start + TIEMPO/1000000;

    while (end - start > 0) {

        printf("Durmiendo durante %d segundos.\n", end-start);
        usleep((end-start)*1000000);
        // Función de dormir (en milisegundos), se encuentra en <unistd.h>

        start = (unsigned long)time(NULL);
        if (end - start <= 0) {
            printf("Se ha acabado el tiempo.\n");
            break;
        }
        printf("Señal recibida, faltan %d segundos.\n", end - start);
    }

    printf("La señal SIGUSR1 fue lanzada %d veces.\n", CONTADOR_SIGUSR1);

    return 0;
}