#include <stdio.h>
#include <stdlib.h>  // exit()
#include <string.h>  // strlen(), memset()

// Las bibliotecas del sistema pueden estar en varias
// localizaciones. Búscalas con:
// find /usr/include -name socket.h

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h> // función close()

/* El siguiente script toma como parámetro un puerto
    donde servirá conexiones el servidor TCP
 */

int main(int argc, char **argv) {
    if(argc > 1) {

        // Definimos dos descriptores de archivo, el puerto
        // y la longitud de la dirección del cliente
        int fd, fd2, puerto, client_len, msg_size, i=0;
        char client_msg[100];
        puerto = atoi(argv[1]);  // Pasamos el puerto como parámetro al script

        // Necesitamos dos esctructuras del tipo socketaddr_in,
        // las cuales se encuentran definidas dentro de <netinet/in.h>
        // La primera guarda la información del servidor y la segunda del cliente
        struct sockaddr_in server, client;

        // Configuración del servidor
        /* Nota: Las funciones htons (host to network short) y htonl (host to network long)
        sirven para convertir datos de tipo int que van a ser enviados a internet,
        esta converción es necesaría para hacer portable el programa en diferentes
        arquitecturas de procesador. Se encuentran en el archivo <netinet/in.h> */
        server.sin_family = AF_INET;      // Familia TCP/IP
        server.sin_port = htons(puerto);  // Puerto
        server.sin_addr.s_addr = INADDR_ANY; // Cualquier cliente puede conectarse (ver <netinet/in.h>)

        // Definimos el socket:
        /* Realiza una llamada al sistema. Esta función devuelve un descriptor de archivo,
        al igual que la función open() al crear o abrir un archivo . Durante la llamada se
        reservan los recursos necesarios para el punto de comunicación, pero no se especifica
        nada con respecto a la dirección asociada al mismo.
        Toma 3 parámetros: el dominio, el tipo de socket y el protocolo.
        El dominio esecifica la familia de protocolo que se usará para la comunicación,
            las cuales se definen en <sys/socket.h>.
        El tipo de socket elegido es de flujo, característico de los sockets TCP.
        Dejando el tercer parámetro a 0, el protocolo se selecciona automáticamente.
        Para más información consultar: man socket */
        fd = socket(AF_INET, SOCK_STREAM, 0);
        if ( fd < 0) {  // Comprobamos si da error
            printf("Error de apertura de socket.\n");
            exit(-1);   // Si es así avisamos y salimos con código de error
        } else {
            printf("Socket creado correctamente.\n");
        }

        // Enlazamos el descriptor del socket a la dirección del servidor
        /* La función bind() toma 3 parámetros:
             - Descriptor de archivo: el archivo abierto del socket.
             - Dirección del socket: del tipo sockaddr tal y como se definen
                 dentro de <netinet/in.h>. Es un puntero.
             - Tamaño de la dirección del socket. */
        if ( bind(fd, (struct sockaddr*) &server, sizeof(struct sockaddr)) == -1) {
            printf("Error en bind()\n");
            exit(-1);
        }

        // Ponemos al socket en modo escucha aceptando un máximo de 1 conexión
        if ( listen(fd, 1) == -1) {
            printf("Error en listen()\n");
            exit(-1);
        } else {
            printf("Esperando conexiones...\n");
        }

        // Aceptamos conexiones
        /* La función accept bloquea la ejecución hasta que se produce
            la conexión con un cliente. Toma 3 parámetros:
                - Descriptor de archivo.
                - Referencia a la dirección del socket.
                - Tamaño de la dirección del socket.
            Devuelve un descriptor de archivo apuntando al socket
            establecido con el cliente. */
        client_len = sizeof(struct sockaddr);
        fd2 = accept(fd, (struct sockaddr*)&client, &client_len);

        if (fd2 == -1) {
            printf("Error en accept()\n");
            exit(-1);
        } else {
            printf("Conexión del cliente aceptada.\n");
            // Enviamos un mensaje de bienvenida al cliente
            printf("< Bienvenido a mi servidor\n");
            send(fd2, "Bienvenido a mi servidor", 26, 0);
        }

        // Mientras los mensajes que nos manda el cliente tengan
        // contenido (significa que la conexión se encuentra abierta)
        while ( (msg_size = recv(fd2, client_msg, 100, 0) ) > 0) {
            // Obtenemos el mensaje del cliente
            printf("> %s\n", client_msg);
        }

        // Cerramos la conexión
        close(fd2);

        if (msg_size == 0) {
            printf("Cliente desconectado.\n");
        } else if (msg_size == -1) {
            printf("Error al recibir un mensaje del cliente.\n");
        }

        // Cerramos el servidor
        close(fd);
        printf("Servidor apagado.\n");

    } else {
        printf("Debes ingresar el puerto que servirá conexiones como parámetro del script.\n");
    }

    return 0;

}
