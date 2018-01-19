## Configuración
El archivo de configuración de nginx se encuentra en `/etc/nginx/nginx.conf`.

### Directivas
Nginx utiliza un lenguaje de directivas que permite organizar y extender los archivos de configuración con facilidad.

#### include
Con este incluimos contenido de otros archivos en el actual, posibilitando modular la configuración.

Permite expresiones regulares. Por ejemplo: `include conf.d/*.conf` incluirá todos los archivos terminados en `.conf` que se encuentren en el directorio `conf.d`.