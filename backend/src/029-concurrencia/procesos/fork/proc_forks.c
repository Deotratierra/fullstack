#include <stdio.h>
#include <sys/types.h>  // Necesaria para usar pid_t
#include <unistd.h>

/* Cuando un programa llama a la función fork(), un proceso duplicado,
    denominado el proceso hijo, es creado. El proceso padre continua
    ejecutando al programa desde el punto en el que el fork fue realizado.
   El proceso hijo también, ejecuta el mismo programa dsde el mismo lugar.
 */

int main () {

    // La función fork() devuelve la ID de un proceso,
    // que es un tipo de dato específico.
    pid_t child_pid;  // También funciona como int
    printf ("El proceso principal del programa es %d\n", getpid());

    // Crear una bifurcación (fork)
    child_pid = fork();

    /* Cuando se crea la bifurcación, al llamar a getpid() desde el proceso
    padre devuelve el ID del proceso hijo, pero al llamarla desde el proceso
    hijo devuelve 0. Ya que ningún proceso puede tener el proceso 0,
    podemos averiguar fácilmente cual es el proceso hijo tras el fork. */
    if (child_pid != 0) {  // Comprobar que se ha producido correctamente
        printf("Este es el proceso padre (PID: %d)\n", getpid());
        printf("El ID del proceso hijo es %d\n", child_pid);
    } else {
        printf("Este es el proceso hijo (PID: %d)\n", getpid());
        printf("La variable child_pid desde el proceso hijo == %d\n", child_pid);
    }

    return 0;
}