// =======================================================================
#include <stdio.h>

/*                  MANEJO DE ARCHIVOS Y DIRECTORIOS EN C               */

// =======================================================================
#ifdef __unix__

#include <sys/stat.h>  // mkdir()

#include <errno.h>
#include <unistd.h>   // access()

/* El manejo de archivos y directorios en Linux con C se realiza a través de
    llamadas al sistema, ubicadas en el fichero de cabecera <unistd.h>. */

int main() {

    // ====================================================================
    //                   Administración de directorios

    /* Crear directorio en C
    Usamos la función mkdir() pasando como primer parámetro el nombre del
        directorio y como segundo un número en notación octal que indicará
        los permisos que se le conceden al nuevo directorio:
    http://pubs.opengroup.org/onlinepubs/009695399/functions/mkdir.html
    */
    mkdir("ejemplo", 0755);


    // ====================================================================
    /*                     Comprobaciones de archivos
    Para realizar diferentes tipos de comprobaciones sobre los archivos
        usamos la función access(). Toma como primer parámetro la ruta a un
        archivo y como segundo una forma de acceder al archivo para realizar
        la comprobación.
   Para más información ejecutar: man access
    */

   // ---------------------------------------------------

    char* archivo = "ff.py";
    int ret;

    // Comprobar la existencia de un archivo
    ret = access(archivo, F_OK);
    if (ret == 0)
        printf ("El archivo %s existe.\n", archivo);
    else {
        if (errno == ENOENT) {
            printf("El archivo %s no existe.\n", archivo);
        } else if (errno == EACCES) {
            printf("El archivo %s no es accesible", archivo);
        } else {
            printf("Valor de retorno desconocido comprobando existencia de archivo: %d\n", ret);
        }
    }

    // ===================================================================

    return 0;
}

#endif

/* Fuentes:
Programación avanzada en Linux - Mark Mitchell, Jeffrey Oldham y Alex Samuel

http://pubs.opengroup.org/onlinepubs/009695399/functions/mkdir.html
*/