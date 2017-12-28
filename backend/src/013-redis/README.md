## Redis

Las instrucciones de instalación [se encuentran aquí](https://redis.io/topics/quickstart):

```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
make test
sudo make install
```

- Para lanzar el servidor: `redis-server`
- Para comprobar que está corriendo: `redis-cli ping`
- Para conectarnos: `redis-cli`
- Para desconectarnos: `exit`
- [Comandos de Redis](https://redis.io/commands)

_________________________________________________


### Canales
Redis posee soporte para crear canales y suscribirse a los mensajes de llegan a los mismos. Podemos comprobarlo abriendo dos consolas con `redis-cli`. En la primera ejecutamos `subscribe advertencias` donde *advertencias* es el nombre del canal que estamos creando. En la segunda publicamos un mensaje con `publish advertencias "Mensaje de advertencia"` y debería aparecer el mensaje también en la primera.

Puedes subscribirte a varios canales (`subscribe channel1 channel2`...)subscribirte a un patrón de canales (`psubscribe warnings:*`) y usar los comandos `unsubscribe` y `punsubscribe` para dejar de escuchar uno o más canales, o un patrón de canales respectivamente.

### Monitorizar
Para ver los comandos que se están ejecutando en la base de datos en tiempo real, simplemente abrimos un nuevo cliente y ejecutamos `monitor`.

