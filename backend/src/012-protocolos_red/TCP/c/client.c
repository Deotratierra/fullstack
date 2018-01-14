#include <stdio.h>
#include <stdlib.h>  // exit()
#include <string.h>  // strlen()

// Las bibliotecas del sistema pueden estar en varias
// localizaciones. Búscalas con:
// find /usr/include -name socket.h

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h> // función close()
#include<arpa/inet.h> //inet_addr

/* Cliente para establecer una conexión TCP a un servidor.
El script toma dos parámetros de entrada, una IP y un puerto */

int main(int argc, char *argv[]) {

    if (argc > 2) {
        // Definimos variables para la ip, el descriptor de archivo,
        // el ¿número de bytes? el puerto (pasado como parámetro)
        // y un buffer de 100 caracteres
        char *ip, buf[100];
        int fd, msg_size, puerto, i=0;
        ip = argv[1],
        puerto=atoi(argv[2]);

        // Información sobre la dirección del servidor
        struct sockaddr_in server;


        // Definimos el socket
        fd = socket(AF_INET, SOCK_STREAM, 0);
        if (fd == -1) {
            printf("socket() error\n");
            exit(-1);
        } else {
            printf("Socket creado correctamente.\n");
        }

        // Datos del servidor
        server.sin_family = AF_INET;
        server.sin_port = htons(puerto);
        server.sin_addr.s_addr = inet_addr(ip);

        // Conectamos con el servidor
        if ( connect(fd, (struct sockaddr *)&server, sizeof(struct sockaddr)) == -1) {
            printf("Error de conexión con el servidor.\n");
            printf("Asegúrate que está encendido en la IP %s y aceptando ", ip);
            printf("conexiones a través del puerto %d\n", puerto);
            exit(-1);
        } else {
            printf("Conexión establecida con el servidor.\n");
        }

        while (1) {
        	// Recibimos datos del servidor
	        msg_size = recv(fd, buf, 100, 0);
	        if (msg_size == -1) {
	            printf("recv() error\n");
	            exit(-1);
	        } else {
	        	// Si no hay error, imprimimos el mensaje que nos envía
	            printf("> %s\n", buf);

	            // Limpiamos el buffer
	            while (i != 100) {
				    buf[i] = 0;
				    i++;
				}
				i = 0;
	        }

            // Enviamos un mensaje, controlando si hay un fallo
            if ( send(fd, "OFF", 3, 0) < 0 ) {
            	printf("Fallo al enviar mensaje al servidor\n");
            } else {
                // Si no da fallo, imprimimos el mensaje que hemos enviado
                printf("< %s\n", "OFF");
            }

            break;
        }

        // Cerramos la conexión
        close(fd);
        printf("Conexión cerrada.\n");

    } else {
        printf("Debes ingresar la IP y el puerto como parámetros del script.\n");
    }

    return 0;
}
