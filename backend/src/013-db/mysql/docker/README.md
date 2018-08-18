## Instalación y despliegue de MariaDB mediante Docker

#### [Referencia oficial en Dockerhub](https://hub.docker.com/_/mariadb/)

- Instalar la última versión estable: `docker pull mariadb:latest`

__________________________

Al instalarlo debemos saber qué puertos expone hacia afuera para poder conectarnos con la base de datos desde fuera del contenedor. Para ello ejecutamos: `docker inspect mariadb:latest | grep -i tcp`

Para correrlo ejecutamos:
```
docker run -dti -p 33306:3306 --name <nombre> -e MYSQL_ROOT_PASSWORD=<contraseña> mariadb:latest
```

> Con la opción `-d` del comando `run` le indicamos que corra en segundo plano.

Debería estar corriendo: `docker ps -a`

__________________________

### Comandos
- Reiniciar: `docker restart <nombre>`
- Detener: `docker stop <nombre`
- Iniciar: `docker start <nombre>`
- Pausar: `docker pause <nombre>`
- Continuar: `docker unpause <nombre>`
- Acceder a los logs del contenedor: `docker logs <nombre>`
