#include <stdio.h>
#include <sys/socket.h>
/* La cabecera de sockets suele estár en '/usr/include/sys/socket.h'
    (en mi caso '/usr/include/x86_64-linux-gnu/sys/socket.h') en Linux. */


int main() {

    // ===========================================================
    //                    Crear un socket             (man socket)
    // int socket (int __domain, int __type, int __protocol)

    int sock;
    sock = socket(PF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        printf("¡Ocurrió un error creando el socket!\n");
    } else {
        printf("El socket se ha creado correctamente\n.");
    }

    /* El parámetro domain especifica el dominio de comunicaciones.
        En este caso se usa PF_INET (protocol family internet), que
        indica la familia de protocolos de internet IPv4.
    EL parámetro type indica el tipo de socket, en este caso un socket
        TCP (canal de comunicación de flujo).
    El  protocolo  especifica  un  protocolo  particular para ser usado
        con el conector. Normalmente sólo existe un protocolo que admita
        un tipo particular de conector dentro de una familia de protocolos dada,
        en cuyo caso protocolo se puede usar 0 para definirse automáticamente.

    La función socket devuelve un descriptor de archivo que funciona como
        un archivo abierto en el cual podemos escribir y leer datos. Si el
        número del descriptor es menor a 0 es que ha sucedido un error.
    */

    // ===================================================================

}
