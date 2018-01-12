#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/* Las funciones exec reemplazan un programa corriendo en un proceso con otro programa.
    Cuando un programa llama a una función exec, ese proceso termina ejecutando
    al programa llamado por exec, asumiendo que la llamada a exec no encontró un error.
    Estas funciones nunca retornan a no ser que la llamada produzca un error.

    Funciones de la familia exec ( https://www.python-course.eu/forking.php ):
        - Las funciones que contienen la letra p (execvp(), execlp(), execlpe() y execvpe())
            aceptan un nombre de programa y buscan el programa en el PATH de ejecución,
            (variable de entorno $PATH). Las funciones que no contienen p deben pasar el
            path completo del programa que desean ejecutar.
        - Las funciones que contienen la letra v (execv(), execve(), execvp() y execvpe())
            aceptan una lista de argumentos para e nuevo programa como un array de punteros
            a cadenas terminado en NULL.
        - Las funciones de contienen la letra l (execl(), execle(), execlp() y execlpe())
            aceptan la lista de argumentos usando el mecanismo varargs del lenguaje C.
        - Las funciones que contienen la letra e (execle(), execve() y execvpe())
            aceptan un argumento adicional, un array de variables de entorno. El argumento
            debe ser un array de punteros a cadenas terminado en NULL. Cada cadena debe
            ir en la forma "VARIABLE=valor".

   Es común usar exec junto a fork para generar un programa que se ejecute en un proceso hijo,
    dejando al proceso padre continuar la ejecución del programa principal:
*/

int main() {
    char *lista_de_argumentos[] = {
    	"ls",   // argv[0] es el nombre del programa
        "-l",   // argv[1]
        "/",
        NULL    // La lista de argumentos debe terminar con NULL
    };

    pid_t child_pid;

    child_pid = fork();
    if (child_pid != 0) {
        printf("Este es el proceso padre (PID: %d)\n", getpid());
    } else {
        // Ejecutar un programa con lista de argumentos buscándolo en el path
        execvp(lista_de_argumentos[0], lista_de_argumentos);
        // El programa se queda abierto mostrando los archivos en el directorio raíz

        // Solo retorna si ocurre un error, por lo tanto esto no se ejecutará
        // si todo sale bien:
        fprintf(stderr, "Ocurrió un error en execvp\n");
        abort(); // Abortamos la ejecución
    }

    printf("El programa principal ha terminado\n");

    return 0;
}
