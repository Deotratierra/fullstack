## Instalar imágenes de versiones de Debian

#### [Referencia oficial en Dockerhub](https://hub.docker.com/_/debian/)

- Última versión de Debian: `docker pull debian:latest`
- Versión estable de Debian: `docker pull debian:stable`
- Debian *Stretch*: `docker pull debian:stretch`
- Debian *Jessie*: `docker pull debian:jessie`
- Debian *Wheezy*: `docker pull debian:wheezy`

La versión `latest` siempre apunta al último lanzamiento estable. Las versiones estables también están etiquetadas con su número de versión, es decir, que ejecutando `docker pull debian:9` instalaremos *stretch*, con `debian:7` *wheezy*...

Existen una variante de las distribuciones que no incluyen archivos extra como la documentación o las páginas *man* que no se suelen requerir en los contenedores, lo que aumenta la velocidad del `pull`. Para obtenerlas simplemente agregamos `-slim` a la versión que queremos, tal que para obtener la última estable: `docker pull debian:stable-slim`.

Vienen incorporadas las locales `C`, `C.UTF-8` , y `POSIX` por defecto.

___________________________________________________

### Utilidades

- Obtener el número de versión de la distribución: `cat /etc/debian_version`.
- Consultar información sobre la versión de la distribución: `cat /etc/os-release`

___________________________________________________

