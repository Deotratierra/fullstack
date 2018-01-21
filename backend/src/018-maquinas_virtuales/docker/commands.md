## Comandos de Docker CE

### Información
- Información de docker: `docker info`
- [Inspeccionar imagen](https://docs.docker.com/engine/reference/commandline/inspect/) (info de bajo nivel): `docker inspect <repo/id>`

### Imágenes
- [Listar imágenes instaladas](https://docs.docker.com/engine/reference/commandline/images/): `docker images`
- [Buscar imágenes](https://docs.docker.com/engine/reference/commandline/search/): `docker search <repositorio>`
- [Descargar imagen](https://docs.docker.com/engine/reference/commandline/pull/): `docker pull <repositorio>`
- [Cambiar nombre a una imagen](https://docs.docker.com/engine/reference/commandline/tag/): `docker tag <id> <nuevo_nombre_repo>:<etiqueta>`
- [Eliminar imagen](https://docs.docker.com/engine/reference/commandline/rmi/): `docker rmi <id>`
- Eliminar todas las imagenes: `docker rmi -f $(docker images -q)`

### Contenedores
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