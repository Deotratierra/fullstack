## Docker
Es una tecnología que consiste en la ejecución de sistemas operativos dentro de otros, obteniendo los sistemas “invitados” su propio sistema de ficheros, su propio espacio de usuarios, sus propios procesos y sus propias interfaces de red, pero compartiendo algunos elementos de la máquina anfitriona como el kernel.

Para separar los contenedores entre sí y de la máquina anfitriona, Docker utiliza las características de aislamiento del kernel Linux. Todo este enfoque permite a los contenedores ser mucho más ligeros que las máquinas virtuales, tanto en espacio en disco como de consumo de recursos. Además su naturaleza les otorga una gran portabilidad y seguridad. Su principal función es la de poder empaquetar aplicaciones con todas las partes necesarias, incluyendo bibliotecas y dependencias.

________________________

### [Instalación](https://docs.docker.com/engine/installation/)

- [Instalación en RaspberryPi](https://github.com/mondeja/fullstack/tree/master/backend/src/018-docker/os/raspberrypi/install.md)

________________________

### Comandos
#### Información
- Información de docker: `docker info`
- [Inspeccionar imagen](https://docs.docker.com/engine/reference/commandline/inspect/) (info de bajo nivel): `docker inspect <repo/id>`

#### Imágenes
- [Listar imágenes instaladas](https://docs.docker.com/engine/reference/commandline/images/): `docker images`
- [Buscar imágenes](https://docs.docker.com/engine/reference/commandline/search/): `docker search <repositorio>`
- [Descargar imagen](https://docs.docker.com/engine/reference/commandline/pull/): `docker pull <repositorio>`
- [Cambiar nombre a una imagen](https://docs.docker.com/engine/reference/commandline/tag/): `docker tag <id> <nuevo_nombre_repo>:<etiqueta>`
- [Eliminar imagen](https://docs.docker.com/engine/reference/commandline/rmi/): `docker rmi <id>`
- Eliminar todas las imagenes: `docker rmi -f $(docker images -q)`

#### Contenedores
- [Correr contenedor accediendo a él](https://docs.docker.com/engine/reference/commandline/run/): `docker run -i <repositorio/id>`
- Salir del contenedor deteniéndolo: `exit`
- Salir del contenedor sin detenerlo: `Ctrl + [P-Q]` (Sin soltar control: pulsamos P, soltamos P, pulsamos Q)
- [Listar contenedores creados](https://docs.docker.com/engine/reference/commandline/ps/): `docker ps -a`
- [Correr contenedor sin acceder a él](https://docs.docker.com/engine/reference/commandline/start/): `docker start <nombre/id>`
- [Acceder a un contenedor creado](https://docs.docker.com/engine/reference/commandline/attach/): `docker attach <nombre/id>`
- [Detener contenedor](https://docs.docker.com/engine/reference/commandline/stop/): `docker stop <nombre/id>`
- [Reiniciar contenedor](https://docs.docker.com/engine/reference/commandline/restart/): `docker restart <nombre/id>`
- [Pausar contenedor](https://docs.docker.com/engine/reference/commandline/pause/): `docker pause <nombre/id>`
- [Continuar contenedor pausado](https://docs.docker.com/engine/reference/commandline/unpause/): `docker unpause <nombre/id>`
- [Guardar la imagen de un contenedor](https://docs.docker.com/engine/reference/commandline/commit/): `docker commit <id> <nuevo_nombre_repo>:<etiqueta>`
- [Eliminar contenedor](https://docs.docker.com/engine/reference/commandline/rm/): `docker rm <id/nombre>`
- Eliminar todos los contenedores: `docker rm $(docker ps -a -q)`
- [Mostrar los logs de un contenedor](https://docs.docker.com/engine/reference/commandline/logs/#options): `docker logs <nombre/id>`


> Cada vez que ejecutamos un contenedor lo estamos creando. Para borrar una imagen necesitamos eliminar los contenedores creados asociados a ella.

#### Combos útiles
- Eliminar todas las imágenes y contenedores: `docker rm -f $(docker ps -a -q) && docker rmi -f $(docker images -q)`

________________________

### Creación de imágenes
Las archivos Dockerfile son scripts que contienen comandos declarados sucesivamente que serán ejecutados, en el orden dado, por Docker para crear automáticamente una nueva imagen. Por ejemplo:
```
FROM resin/rpi-raspbian
USER root

RUN apt-get update && \
    apt-get -qy install ca-certificates python python-pip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qy clean all
CMD ["python"]
```

- [Referencia Dockerfile](https://docs.docker.com/engine/reference/builder/#cmd)

#### Construir imágenes en local
- Para correr una imagen creada localmente: `docker build <ruta/al/DIRECTORIO/donde/se/encuentra/el/Dockerfile>`.
- Para reiniciar la construcción de la imagen: `docker build . --no-cache`

##### [Construcción de imágenes por sistema operativo y distribución](https://github.com/mondeja/fullstack/tree/master/backend/src/018-docker/os)

________________________


> Fuentes:
> - https://docs.docker.com
> - https://www.muylinux.com/2016/04/19/tutorial-docker/
> - https://www.digitalocean.com/community/tutorials/docker-explicado-como-crear-contenedores-de-docker-corriendo-en-memcached-es

