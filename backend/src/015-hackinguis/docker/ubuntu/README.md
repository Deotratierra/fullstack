## Ubuntu con noVNC
- Correr directamente: `docker run -it --rm -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc`
- Correr protegiendo VNC con contraseña: `docker run -it --rm -p 6080:80 -p 5900:5900 -e VNC_PASSWORD=mypassword dorowu/ubuntu-desktop-lxde-vnc`

Luego de ejecutar uno de los comandos anteriores ir a http://127.0.0.1:6080/.

- Acceder al contenedor (debemos correrlo con la opción `-d`): `docker exec -it <machine_id> bash`

____________________________________

> Fuentes:
> https://github.com/fcwu/docker-ubuntu-vnc-desktop