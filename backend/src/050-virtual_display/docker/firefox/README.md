## Desplegar Firefox en un contenedor Docker

- Construir la imagen Docker de este directorio: `docker build -t firefox .`
- Ejecutar:
```
docker run -ti --rm \
       -e DISPLAY=$DISPLAY \
       -v /tmp/.X11-unix:/tmp/.X11-unix \
       firefox
```

> Fuente:
> http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/