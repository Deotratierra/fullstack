#include <sys/socket.h>
#include <arpa/inet.h>  // inet_aton()

// ================================================================================

/* Las estructuras de datos en la red siguen una ordenación de bytes
Big Endian.

Las estructuras de datos usadas en direcciones de socket son las siguientes:
*/

int main() {
    // Estructura de dirección de socket básica
    struct sockaddr {
        unsigned short sa_family;  // Familia de direcciones (AF_...)
        char           sa_data[14] // 14 bytes de la dirección del protocolo
    } /* Esta estructura resulta farragosa, ya que tenemos que empaquetar a
          mano la dirección IP y el puerto en el campo sa_data. Por ello, para
          las direcciones de internet se utiliza la siguiente: */

    // Estructura de dirección de socket de internet
    struct sockaddr_in {
        short int          sin_family;   // Familia de direcciones: AF_INET
        unsigned short int sin_port;     // Número de puerto
        struct in_addr     sin_addr;     // Dirección de internet
        unsigned char      sin_zero[8];  // Relleno para preservar el tamaño
    }
    /* sin_zero se incluye para que la nueva estructura tenga el mismo tamaño
        que struct sockaddr y debe rellenarse todo a ceros usando la función memset().
    Un puntero a struct sockaddr_in puede forzarse (cast) a un puntero a struct sockaddr
        y viceversa. Así, aunque la función socket() exige un struct sockaddr*, puedes
        usar un struct sockaddr_in y forzarlo en el último momento.
    sin_port y sin_addr deben seguir la ordenación de bytes de la red (big endian). */

    // ===============================================================================

    //            Rutinas de conversión de direcciones a Big Endian
    /* Existen dos tipos sobre los cuales podemos aplicar la conversión: short (dos bytes)
        y long (cuatro bytes).
    Imagina que quieres convertir un short desde la Ordenación de máquina [Host Byte Order]
        a la Ordenación de la red [Network byte order]. Empieza con una "h" de "host",
        síguela con "to" (a, hacia,...), luego una "n" de "network " y finalmente una "s"
        de "short": h-to-n-s, es decir, htons() ("Host to Network Short", short del host
        al de la red):

    htons() -- "Host to Network Short " (short de máquina a short de la red)
    htonl() -- "Host to Network Long" (long de la máquina a long de la red)
    ntohs() -- "Network to Host Short " (short de la red a short de máquina)
    */

    // ===============================================================================

    // Dada una estructura de socket de dirección de internet
    struct sockaddr_in direccion;

    // Podemos definirla de la siguiente forma:
    direccion.sin_family = AF_INET;
    direccion.sin_port = htons(8000);  // Conversión a short big endian
    direccion.sin_addr.s_addr = inet_addr("10.12.110.57");
    //inet_aton("10.12.110.57", &(direccion.sin_addr));
    memset(&(direccion.sin_zero), '\0', 8);

    /* La función inet_addr() convierte una dirección IP dada la notación de cifras
    y puntos en un unsigned long (su representación binaria).
    También podemos usar la función inet_aton() ("ASCII to network"). Se puede realizar
    el camino contrario (de binario a ASCII) con la función inet_ntoa(): */
    printf("%s", inet_ntoa(direccion.sin_addr));

    /* Fíjate en que inet_ntoa() toma un struct in_addr como argumento, y no un long.
        Date cuenta también de que devuelve un puntero a char. Éste apunta a una zona
        estática de memoria dentro de inet_ntoa(), así que cada vez que llames a inet_ntoa()
        se perderá la última dirección IP que pediste. Por ejemplo:

    char *a1, *a2;

    a1 = inet_ntoa(ina1.sin_addr);  // esta es 192.168.4.14
    a2 = inet_ntoa(ina2.sin_addr);  // esta es 10.12.110.57   Imprime:
    printf("address 1: %s\n",a1);                             // 10.12.110.57
    printf("address 2: %s\n",a2);                             // 10.12.110.57

    Si necesitas conservar la dirección, usa strcpy() para copiarla a tu propia variable.
        Para saber que cabeceros debes incluir para utilizar estas funciones en tu sistema,
        revisa las páginas del manual.
    */

    return 0;
}