## Instalar imágenes de versiones de CentOS

#### [Referencia oficial en Dockerhub](https://hub.docker.com/_/centos/)

- Obtener la última versión estable: `docker pull centos:latest`
- CentOS 7; `docker pull centos:7`
- CentOS 6: `docker pull centos:6`

_______________________________________

### Utilidades

- Consultar información sobre la versión de la distribución: `cat /etc/os-release`
- Consultar el número de versión de la distribución: `cat /etc/centos-release | cut -d " " -f 4`