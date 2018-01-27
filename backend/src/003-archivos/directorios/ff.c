// =======================================================================
#include <stdio.h>

/*                  MANEJO DE ARCHIVOS Y DIRECTORIOS EN C               */

// =======================================================================
#ifdef __unix__

#include <sys/stat.h>  // mkdir()

#include <errno.h>
#include <unistd.h>    // access()

#include <dirent.h>    // DIR

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

    // ------------------------------------------------------------------

    /* Abrir un directorio
    Para leer el contenido de un directorio en C primero hemos de abrirlo.
        Esto se realiza con la función opendir(), la cual recibe como parámetro
        la ruta al directorio y devuelve un manejador del directorio, el cual
        deberá ser declarado como puntero de tipo DIR. Este tipo está definido
        en el cabecero <dirent.h>.
    */
    DIR* p_directorio;            // Puntero al directorio
    char* ruta_directorio = ".";  // Ruta al directorio (en este caso el actual)

    p_directorio = opendir(ruta_directorio);  // Abrir el directorio
    if (p_directorio == NULL) {   // Comprobar si sucedió un error
        printf("Ocurrió un error al abrir el directorio %s\n", ruta_directorio);
    } else {
        printf("El directorio %s se abrió correctamente.\n", ruta_directorio);
    }


    /* Leer directorio
    Para leer un directorio usamos la función readdir(), la cual toma un puntero
        al directorio que queremos leer y devuelve una estructura dirent,
        la cual está definida en el cabecero dirent.h. Para leer por los archivos
        del directorio sólo tenemos que crear un bucle while para que el
        puntero vaya incrementando de nodo en nodo hasta que llegue a uno nulo,
        lo cual indica el final del directorio.
        http://pubs.opengroup.org/onlinepubs/7908799/xsh/readdir.html
        Otra información: man readdir
    Los mimebros de la estructura dirent son:
        - d_name (char): Nombre del archivo (es el único campo que,
            según GNU, se encuentra en todas las distribuciones y asegura
            el cumplimiento del estándar POSIX).
        - d_ino (ino_t): Número de serie del archivo dentro del sistema
            (número único para cada archivo).
        - d_reclen/d_namlen (unsigned char): Cantidad de bits que ocupa el
            nombre del archivo.
        - d_off (off_t): Número sólo interpretable por el sistema que apunta
            a la siguiente entrada en el directorio.
        - d_type (unsigned char): Tipo de archivo. Un 4 representa un directorio
            y un 8 representa un archivo. Para ver una lista de los tipos posibles:
    https://www.gnu.org/software/libc/manual/html_node/Directory-Entries.html
    */
    struct dirent* p_dirent;

    while( (p_dirent = readdir(p_directorio)) != NULL) {
        printf("%d\t%d\t%d\t%s\t%d\n", p_dirent->d_ino, p_dirent->d_off,
                                   p_dirent->d_reclen, p_dirent->d_name,
                                   p_dirent->d_type);

    }

    // Cerrar directorio
    closedir(p_directorio);  // Siempre cerrar el búffer cuando no se necesite


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
https://baulderasec.wordpress.com/programacion/programacion-con-linux/3-trabajando-con-los-archivos/escaneo-de-directorios/opendir/ejemplo-opendir/
http://pubs.opengroup.org/onlinepubs/7908799/xsh/readdir.html
http://pubs.opengroup.org/onlinepubs/009695399/basedefs/dirent.h.html
https://www.gnu.org/software/libc/manual/html_node/Directory-Entries.html
*/