## Instalación de XAMPP

### Linux
1. Vamos a la [página de descargas de XAMPP](https://www.apachefriends.org/download.html) y descargamos la versión Linux que deseamos.
2. Para ejecutar el instalador desde consola primero debemos establecer permisos de ejecución con `chmod 500`.
3. Al instalar te dará la opción de ejecutar el panel de control de XAMPP. Para volver a abrirlo ejecutamos `sudo /opt/lampp/./manager-linux-x64.run`.

- El programa de instalación te indicará donde será instalado XAMPP. En caso de sistemas Unix a día de hoy se instala en `/opt/lampp`. Allí se encuentran los binarios con los que podemos controlar los servidores.

#### Comprobar la instalación
Si has has instalado tu distribución de Linux con un servidor web incorporado por defecto, entonces lo más seguro es que Apache2 esté instalado y configurado para empezar a ejecutarse como al encender la máquina. Por lo que si vas al panel de control de XAMPP e intentas correr el servidor web, este se detendrá.

Para solucionarlo primero vamos a la dirección `http://localhost` en el navegador. Si ves la típica ventana de inicialización de Apache, es que Apache2 está corriendo en el puerto 80 y no deja a XAMPP lanzar su servidor en el mismo puerto. Esto podemos comprobarlo ejecutando `sudo service apache2 status`. Si está corriendo el servicio ejecuta `sudo service apache2 stop` y ahora sí podrás lanzar el servidor desde el panel de control de XAMPP. Cuando lo lances vuelve a `http://localhost` y, si todo ha ido bien, debería redireccionarte a `http://localhost/dashboard/` y aparecería algo así como "Welcome to XAMPP for Linux <version>".

_______________________________

### Windows
1. Vamos a la [página de descargas de XAMPP](https://www.apachefriends.org/download.html) y descargamos la versión Windows que deseamos que deseamos.
2. Ejecutamos el archivo que hemos descargado e instalamos el programa con todos las extensiones añadidas que necesitamos.
3. XAMPP se instalará en la ruta `C:\xampp`, donde puedes encontrar el binario para abrir el panel de control.

#### Comprobar la instalación
Simplemente inicia el servidor y ve a `http://localhost` y, si todo ha ido bien, debería redireccionarte a `http://localhost/dashboard/` y aparecería algo así como "Welcome to XAMPP for Windows <version>".

Es probable que, al intentar iniciar el servidor, Apache2 te muestre el error `Apache shutdown unexpectedly` y lo más seguro es porque está configurado para escuchar en los puertos `80` y `443` pero estos ya están ocupados por aplicaciones del sistema.

Para cambiar los puertos de escucha cambia en el archivo `httpd.conf` las líneas `Listen 80` y `ServerName localhost:80` (cambia el puerto 80 por el que quieras) y en el archivo `httpd-ssl.conf` las líneas `Listen 443`, `<VirtualHost _default_:443>` y `ServerName www.example.com:443` (cambia el puerto 443 por el que quieras). Ten en cuenta que ahora deberás acceder a `http://localhost:80` cambiando el `80` por el número del puerto que pusiste al cambiarlo.