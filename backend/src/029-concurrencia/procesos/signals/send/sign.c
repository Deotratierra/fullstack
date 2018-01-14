#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>  // exit(), abort()
#include <ctype.h>

/* Para enviar una señal a un proceso, al igual que en Bash,
    usamos la función kill() */

int main() {
    pid_t child_pid;

    char respuesta;
    int respuesta_valida = 0;

    child_pid = fork();

    if (child_pid != 0) {
        printf("Proceso padre durmiendo durante 3 segundos...\n");
        usleep(3 * 1000000);

        printf("Proceso padre se despierta.\n");
        usleep(2 * 1000000);

        while (respuesta_valida == 0) {
        	printf("Estás en el proceso padre. ¿Quieres matar a tu hijo? S/N: ");
	        scanf("  %c", &respuesta);

	        respuesta = toupper(respuesta);
            if ( (respuesta == 'S') || (respuesta == 'N') ) {
                respuesta_valida = 1;
            } else {
                printf("Respuesta inválida.\n");
                continue;
            }

            if (respuesta == 'S') {
	            printf("El padre, que le da a la bebida, mata al hijo.\n");

	            // Enviar una señal
                kill(child_pid, SIGKILL);

	            // Realmente no tendrá efecto si el hijo se ha despertado y ha
	            // terminado, pero no se producirá ningún error

	            usleep(2 * 1000000);
	            printf("El proceso padre llora arrepentido.\n");
	        } else {
	            kill(child_pid, SIGKILL);
	            printf("El proceso padre se vuelve a acostar.\n");
	            usleep(15 * 1000000);

	            printf("El proceso padre se levanta recordando la pesadilla de anoche.\n");
            }
        }

    } else {
	    printf("Proceso hijo durmiendo durante 20 segundos...\n");
	    usleep(20 * 1000000);

	    // Esta ejecución no se producirá si lo matamos
	    printf("\nEl proceso hijo se levanta, desayuna y se va al colegio.\n");

	    exit(0);
    }

    usleep(2 * 1000000);
    printf("FIN DE LA HISTORIA\n\n");

    // ===================================================
    //           Señales al proceso actual

    // SIGTERM
    exit(0)

    // SIGABRT
    abort()

    /* Podemos lanzar cualquier señal al proceso actual usando
    la función raise(), pasándole como primer parámetro un entero
    con el número de la señal (o su nombre en <signal.h>). */
    raise(SIGTSTP)

    return 0;
}

