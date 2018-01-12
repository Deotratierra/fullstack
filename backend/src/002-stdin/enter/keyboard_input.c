#include <stdio.h>
#include <string.h>  // strchr()


void limpiar (char *cadena)
{
  char *p;
  p = strchr(cadena, '\n');  // Busca el salto de línea en la cadena
  if (p)
    *p = '\0';
}

int main() {
    // =========================================================================
    // ENTRADA BÁSICA POR TECLADO

    char nombre[30];

    printf("Escribe tu nombre: ");
    // scanf("%s", &nombre);  // <-- No funciona si hay un espacio en el nombre
    fgets(nombre, 30, stdin); // <-- Lee también el caracter ENTER (salto de línea),
    limpiar(nombre);          //     por eso hay que eliminarlo (ver la fuente)

    printf("Bienvenid@ a mi documentación, %s.\n", nombre);

    // ==========================================================================

    return 0;
}

/* Fuente:
https://batchdrake.wordpress.com/2008/03/03/como-leer-lineas-de-texto-del-teclado-en-c/
*/