## [Stream sockets](https://en.wikipedia.org/wiki/Stream_socket) (Sockets de flujo)
Provee una conexión orientada, secuencial y un único flujo de datos sin límites de registro, con mecanismos bien definidos para crear y destruir conexiones, así como para detectar errores.

Este tipo de sockets transmiten información de forma fiable, en orden y con capacidades [fuera de banda](https://en.wikipedia.org/wiki/Out-of-band_data).

### Protocolo TCP
Los sockets de flujo usan el protocolo TCP para la transmisión de datos definiendo una comunicación bidireccional, confiable y orientada a la conexión: todo lo que se envíe por un extremo de la comunicación, llegará al otro extremo en el mismo orden y sin errores (existe corrección de errores y retransmisión).