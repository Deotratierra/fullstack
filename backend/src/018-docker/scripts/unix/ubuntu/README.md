## Instalar imágenes de versiones de Ubuntu

#### [Referencia oficial en Dockerhub](https://hub.docker.com/_/ubuntu/)

- Obtener la última versión LTS estable: `docker pull ubuntu:latest`
- Obtener la última versión estable: `docker pull ubuntu:rolling`
- Ubuntu *Artful Aardvark*: `docker pull ubuntu:17.10`
- Ubuntu *Zesty Zapus*: `docker pull ubuntu:17.04`
- Ubuntu *Yakkety Yak*: `docker pull ubuntu:16.10`
- Ubuntu *Xenial Xerus*: `docker pull ubuntu:16.04`

#### [Listado actualizado de versiones de Ubuntu](https://es.wikipedia.org/wiki/Anexo:Versiones_de_Ubuntu)

Vienen incorporadas las locales `C`, `C.UTF-8` , y `POSIX` por defecto.

### Utilidades
- Obtener el número de versión de la distribución: `grep DISTRIB_RELEASE /etc/lsb-release | cut -d = -f 2`
- Consultar información sobre la versión de la distribución: `cat /etc/os-release`
