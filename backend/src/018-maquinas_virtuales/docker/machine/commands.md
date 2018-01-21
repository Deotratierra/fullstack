## Comandos Docker Machine

### Administrar máquinas
- [Listar las máquinas creadas](https://docs.docker.com/machine/reference/ls/): `docker-machine ls`
- [Crear una máquina](https://docs.docker.com/machine/reference/create/): `docker-machine create -d <driver> <nombre_de_la_máquina>`
- Ver las variables de entorno necesarias para activar una máquina: `docker-machine env <nombre_de_la_máquina>`
- Activar una máquina: `eval $(docker-machine env <nombre_de_la_máquina>)`
- Ver la máquina activa: `docker-machine active`
- Encender una máquina: `docker-machine start <nombre_de_la_máquina>`
- Parar una máquina: `docker-machine stop <nombre_de_la_máquina>`
- Conectarnos a una máquina por SSH: `docker-machine ssh <nombre_de_la_máquina>`

### Configuración e información de máquinas
- Obtener la IP de una máquina: `docker-machine ip <nombre_de_la_máquina>`
