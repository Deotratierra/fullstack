## Servidores web Apache

### [Instalación de XAMPP por sistema operativo](https://github.com/mondeja/fullstack/tree/master/backend/src/012-protocolos_red/HTTP/servidor/apache/xampp_install.md)

______________________________

En la mayoría de sistemas Linux actuales Apache2 viene instalado y configurado como servicio para ejecutarse como demonio al encender la máquina. Si con el navegador entras en `localhost` verás que te aparece la página por defecto de Apache2. En ella se explica lo principal que debes saber sobre los archivos de configuración de Apache2, entre otras cosas.

### Archivos de configuración de Apache2

Los archivos de configuración de Apache2 se encuentran en el directorio `/etc/apache2/`, y siguien la siguiente estructura de directorios:
```
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
```

- `apache2.conf`: archivo de configuración principal. Une todas las piezas incluyendo todos los demás archivos de configuración cuando arranca el servidor web.
- `ports.conf`: siempre es incluido en el archivo de configuración principal. Se usa para determinar los puertos escuchando conexiones entrantes y este archivo puede ser personalizado en cualquier momento.
- Los archivos de configuración que se encuentran dentro de los directorios `mods-enabled/`, `conf-enabled/` y `sites-enabled/` contienen pequeños trozos de configuración los cuales administran los módulos, fragmentos de configuración globales o configuraciones de hosting virtual, respectivamente.

_______________________

### Comandos básicos
Para ejecutar el binario de `apache2` puedes usar tanto `/etc/init.d/apache2` como `sudo service apache2`, pero mediante la ejecución del binario `/usr/sbin/apache2` no funcionará ya que no leerá la configuración.

- Ver el estado del servidor: `sudo /etc/init.d/apache2 status`
- Arrancar el servidor: `sudo /etc/init.d/apache2 start`
- Detener el servidor: `sudo /etc/init.d/apache2 stop`
- Reiniciar el servidor: `sudo /etc/init.d/apache2 restart`
- Recargar la configuración: `sudo /etc/init.d/apache2 reload`

_______________________


### Básico
Cuando instalamos Apache mediante XAMPP, éste nos crea una carpeta donde podemos albergar nuestras páginas PHP. Este sitio se conoce como la raíz de los documentos, y por defecto tiene el nombre de `htdocs`. 

En cualquier caso si quisiéramos albergar estas páginas web en otra carpeta podríamos hacerlo mediante el archivo de configuración del fichero de Apache `httpd.conf`. Este archivo también se encuentra en la carpeta en la que instaló apache. Dentro de este archivo, la ubicación de la raíz de documentos se indica en el parámetro `DocumentRoot`.

Por tanto si creáramos una carpeta llamada pruebas en `htdocs`, podríamos acceder a ella mediante `http://localhost/pruebas`.

Pero, ¿qué pasa si quisiéramos albergar nuestras páginas en otra carpeta? Pues solo tendríamos que crear un alias dentro del archivo de configuración. Después de la palabra Alias ponemos el nombre que queramos para entrar a las páginas, y a continuación la ruta donde están albergadas.

> Cada vez que se cambie algún dato del archivo de configuración es necesario reiniciar Apache.

______________________________

### Hosting virtual (múltiples servidores en una máquina)
Los sitios web virtuales pueden estar basados en que cada sitio web tiene una dirección IP diferente, o que una IP funcione varios sitio web virtuales con diferentes nombres de dominios. Esto último pasa totalmente desapercibido para el usuario.

Para usar un alojamiento virtualizado por nombres tendremos que indicar, en el archivo `httpd.conf` de nuestro servidor (Apache), la IP y su puerto, para la escucha de las solicitudes de los diferentes hosts. Para ello usaremos NameVirtualHost.

Dentro de NameVirtualHost, crearemos un bloque en el cuál introduciremos las directivas para identificar el dominio.

```
NameVirtualHost 192.168.1.3:80

ServerName www.dominio1.com
ServerAlias dominio1.com *.dominio1.com
DocumentRoot /www/dominio1

ServerName www.dominio2.com
ServerAlias dominio2.com *.dominio2.com
DocumentRoot /www/dominio2
```

El puerto de escucha es donde nuestro servidor, Apache, espera peticiones entrantes.

Se puede establecer qué puertos, direcciones IP o nombres de hosts se pueden aceptar. Por ejemplo:

```
Listen 80

Listen 192.168.1.25:80

Listen Pepito12:80
```