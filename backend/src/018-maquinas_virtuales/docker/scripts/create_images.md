## Creación de imágenes con Docker

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

### Construir imágenes en local
- Para correr una imagen creada localmente: `docker build <ruta/al/DIRECTORIO/donde/se/encuentra/el/Dockerfile>`.
- Para reiniciar la construcción de la imagen: `docker build . --no-cache`

#### [Construcción de imágenes por sistema operativo y distribución](https://github.com/mondeja/fullstack/tree/master/backend/src/018-maquinas_virtuales/docker/os)