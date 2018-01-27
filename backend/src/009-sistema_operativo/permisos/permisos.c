// =======================================================================
#include <stdio.h>

/*                    MANEJO DE PERMISOS DE ARCHIVOS EN C               */

// =======================================================================
#ifdef __unix__

#include <errno.h>
#include <unistd.h>

int main() {

    // ====================================================================
    /* Comprobaciones de archivos
    Para realizar diferentes tipos de comprobaciones sobre los archivos
        usamos la función access(). Toma como primer parámetro la ruta a un
        archivo y como segundo una forma de acceder al archivo para realizar
        la comprobación.
   Para más información ejecutar: man access
    */

    // ---------------------------------------------------

    // Comprobar permisos de lectura
    ret = access(archivo, R_OK);
    if (ret == 0) {
        printf("El archivo %s es leíble.\n", archivo);
    } else {
        printf("El archivo %s no es leíble (acceso denegado).\n", archivo);
    }

    // --------------------------------------------------

    // Comprobar permisos de escritura
    ret = access(archivo, W_OK);
    if (ret == 0) {
        printf("El archivo %s es escribible.\n", archivo);
    } else if (errno == EACCES) {
        printf("El archivo %s no es escribible (acceso denegado).\n", archivo);
    } else if (errno == EROFS) {
        printf("El archivo %s no es escribible (sólo leíble).\n", archivo)
    } else {
        printf("Valor de retorno desconocido comprobando permisos de escritura en archivo: %d\n", ret);
    }

    // ===================================================================

    return 0;
}

#endif
