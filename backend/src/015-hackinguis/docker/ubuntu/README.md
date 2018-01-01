## Ubuntu por VNC
- Correr directamente: `docker run -it --rm -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc`
- Correr protegiendo con contraseña: `docker run -it --rm -p 6080:80 -p 5900:5900 -e VNC_PASSWORD=mypassword dorowu/ubuntu-desktop-lxde-vnc`

Luego de ejecutar uno de los comandos anteriores ir a http://127.0.0.1:6080/.


> Fuente:
> https://github.com/fcwu/docker-ubuntu-vnc-desktop