## Nginx

- Instalación: `sudo apt-get install nginx`

Por defecto en Linux corre el servidor Apache en el puerto 80, así que debemos cambiarlo para que no de problemas con nginx: `sudo nano /etc/apache2/ports.conf`. También hay que tener en cuenta que si accedemos a la página local en [`localhost:80`](localhost:80) vamos a ver la página por defecto de Apache, [aquí sabrás por qué](https://askubuntu.com/questions/642238/why-do-i-still-see-an-apache-site-on-nginx).

______________________________

### Comandos
Puede ejecutarse como demonio del sistema (systemctl) o como proceso. Elige una de las dos formas, pues con ambas pueden resultar en fallos.

#### Demonio systemctl
- Activar: `sudo service nginx start`
- Terminar: `sudo service nginx stop`
- Reiniciar: `sudo service nginx restart`
- Ver estado: `sudo service nginx status`
- Testear la configuración de nginx: `sudo service nginx configtest`
- Recargar la configuración: `sudo service nginx reload`

#### Como proceso
> El binario ejecutable se encuentra en `/usr/sbin/nginx`.

- Finalizar inmediatamente: `sudo nginx -s stop`
- Finalizar después de atender las peticiones actuales: `sudo nginx -s quit`
- Recargar el archivo de configuración: `sudo nginx -s reload`
- Reiniciar los archivos de registro: `sudo nginx -s reopen`


- Ver los procesos abiertos por nginx: `ps -ax | grep nginx`
- Comprobar si la configuración tiene errores de sintaxis: `sudo nginx -t`

_______________________________
#### Errores de proceso corriendo el ejecutable
- Si te aparece `nginx: [error] open() "/run/nginx.pid" failed (2: No such file or directory)` al ejecutar: `sudo nginx`. Ejecuta: `ps -ef | grep nginx` y mata el proceso raíz de nginx: `sudo kill <PID>`. Esto es la mejor forma de reiniciarlo completamente.
- Si te aparece `nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)` es que debes cerrar el servicio del sistema: `sudo service nginx stop`.

_______________________________

## En profundidad
- #### [Configuración](https://github.com/mondeja/fullstack/tree/master/backend/src/012-protocolos_red/HTTP/servidor/nginx/config.md)
