## Configuración

El archivo de configuración de nginx se encuentra en `/etc/nginx/nginx.conf`.

Hay tres estrategias para balancear o distribuir la carga:

- **round-robin**: las peticiones son distribuidas entre los servidores de forma cíclica. Cabe la posibilidad de que las peticiones más pesadas sean procesadas por el mismo servidor, distribuye las peticiones de forma ecuánime pero la carga no.
- **least-connected**: la siguiente petición es atendida por el servidor con menos conexiones activas.
- **ip-hash**: se selecciona el servidor que atenderá la petición en base a algún dato como la dirección IP, de esta forma todas las peticiones de un usuario son atendidas por el mismo servidor.

> Nginx utiliza un lenguaje de directivas que permite organizar y extender los archivos de configuración con facilidad.

##### include
Con este incluimos contenido de otros archivos en el actual, posibilitando modular la configuración. Permite expresiones regulares. Por ejemplo: `include conf.d/*.conf` incluirá todos los archivos terminados en `.conf` que se encuentren en el directorio `conf.d`.

### Estrategia Round-Robin

```
upstream app {
    server app1:8080;
    server app2:8080;
    server app3:8080;
}

server {
    listen 80;

    location / {
        proxy_pass http://app;
        add_header X-Upstream $upstream_addr;
    }
}
```