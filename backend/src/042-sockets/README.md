## Tipos de socket

### [Stream sockets](https://en.wikipedia.org/wiki/Stream_socket) (Sockets de flujo)
Provee una conexión orientada, secuencial y un único flujo de datos sin límites de registro, con mecanismos bien definidos para crear y destruir conexiones, así como para detectar errores.

Este tipo de sockets transmiten información de forma fiable, en orden y con capacidades [fuera de banda](https://en.wikipedia.org/wiki/Out-of-band_data).

### [Datagram sockets](https://en.wikipedia.org/wiki/Datagram_socket) (Sockets de datagramas)
Los mensajes no tienen el mismo orden de llegada que de salida y la fiabilidad de que lleguen no está garantizada. Los [datagramas](https://es.wikipedia.org/wiki/Datagrama) envían una cabeceran con la dirección de origen y el destinatario, lo que permite enrutar cada fragmente al receptor por rutas diferentes.

#### Ventajas:
- Control de tráfico para aprovechar la [capacidad de canal](https://es.wikipedia.org/wiki/Capacidad_de_canal) de cada tramo de red.
- Adaptarse ante congestiones y caídas de nodos intermedios, evitando bloqueos.
- Abaratar costes, al poder ajustar el ancho de banda y número de líneas precisados.

#### Inconvenientes:
- No hay una velocidad constante en el flujo de datos.
- No está garantizado que los paquetes se reciban en el orden original de salida.
- No está garantizado que todos los paquetes lleguen as su destino.

### [Raw sockets](https://en.wikipedia.org/wiki/Raw_socket) (Sockets crudos)
Permiten la comunicación sin especificar un protocolo de comunicación. Usualmente, las cabeceras suelen estar incluidas al leer de los sockets, al transmitir es opcional incluirlas.

Un uso real de este tipo es sockets está en el envío de [pings](https://es.wikipedia.org/wiki/Ping).

___________________________________________

## Familias de sockets

### [UNIX](https://es.wikipedia.org/wiki/Socket_Unix)
Los sockets de dominio Unix son flujos de bytes usados para la comunicación entre procesos de una máquina.

Utilizan el sistema de archivos como s dirección de espacio de nombres, por lo que son vistos por los procesos como archivos de un sistema de archivos, lo cual permite que dos procesos distintos abran el mismo socket para comunicarse. Sin embargo, el intercambio de datos no utiliza el sistema de ficheros, si no buffers de memoria del núcleo.

### 


> Fuentes:
> - https://en.wikipedia.org/wiki/Stream_socket
> - https://en.wikipedia.org/wiki/Out-of-band_data
> - https://en.wikipedia.org/wiki/Datagram_socket
> - https://es.wikipedia.org/wiki/Datagrama
> - https://es.wikipedia.org/wiki/Capacidad_de_canal
> - https://en.wikipedia.org/wiki/Raw_socket
> - https://es.wikipedia.org/wiki/Ping
> - https://es.wikipedia.org/wiki/Socket_Unix