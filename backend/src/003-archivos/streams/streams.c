#include <stdio.h>

int main() {
    /* Por razones históricas, el tipo de estructura de datos que representa
    un canal (stream) en C es el tipo FILE del cabecero <stdio.h>

    Cuando la función main del programa es invocada, hay tres canales abiertos.
    Estos representan las tres salidas estándar y se encuentran en las variables: */
    FILE *stdin, *stdout, *stderr;

    // Abrir un archivo
    // La función fopen() de stdio.h abre un fichero y devuele un puntero al canal.
    // Toma dos parámetros, el nombre del fichero y el modo de apertura.
    char canal[1024];
    stdout = fopen("../archivo.txt", "x");
    if (canal != 0){
        fscanf(stdout, "%[^\n]", canal);
        printf("%s\n", canal);
    }

	return 0;
}