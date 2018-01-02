#include <stdio.h>

int main() {
    FILE *manejador;
    FILE *manejador2;

    // Abrir un archivo para escritura
    manejador = fopen("ejemplo.txt", "w");
    if (manejador != 0) {
        printf("Archivo abierto para escritura.\n");
        // Escribir en un archivo
        fprintf(manejador, "%s\n", "Contenido del archivo.");
        fclose(manejador);
    } else {
        printf("Ocurrió un error al intentar escribir el archivo.\n");
        if (manejador != NULL) {
            fclose(manejador);
        }
        return 1;
    }

    // Abrir un archivo para lectura
    char buffer[1024];
    manejador2 = fopen("ejemplo.txt", "r");
    if (manejador2 != 0) {
        printf("Archivo abierto para lectura.\n");
        // Leer la primera línea del archivo
        fscanf(manejador2, "%[^\n]", buffer);
        printf("%s\n", buffer);
    } else {
        printf("Ocurrió un error al intentar leer el archivo.\n");
        if (manejador2 != NULL) {
            fclose(manejador2);
        }
        return 1;
    }

    return 0;
}

/* Fuentes:
https://code-reference.com/c/stdio.h/fopen
https://stackoverflow.com/questions/11573974/write-to-txt-file
https://www.programiz.com/c-programming/examples/read-file
*/