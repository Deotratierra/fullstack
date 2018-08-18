## Montar un servidor FTP

### Windows7 mediante IIS
1. [Configuramos la IP como estática](https://github.com/mondeja/fullstack/tree/master/backend/src/012-protocolos_red/IP/static).
2. `Panel de control` -> `Programas` -> `Programas y características` -> `Activar o desactivar características de Windows` -> Activamos todas las casillas de `Internet information services`
3. `Panel de control` -> `Sistema y seguridad` -> `Herramientas administrativas` -> `Administrador de Internet Information Services`. Desde aquí podemos agregar y configurar un nuevo sitio FTP. Vamos a `Conexiones`, elegimos nuestro host -> `Click derecho del ratón` -> `Agregar sitio FTP`. Cuando nos pregunte la IP pondremos la IP estática que configuramos en el paso 1. `Ruta de acceso física` se refiere a la carpeta que será compartida por el servidor.
4. Si queremos acceder desde otro ordenador conectado a la red local debemos desactivar el firewall de Windows para las conexiones entrantes desde la red doméstica, pero esto sólo sería conveniente si separamos el acceso a internet y el acceso a la red local en dos redes diferentes ([como se explica aquí usando VirtualBox](https://github.com/mondeja/fullstack/tree/master/backend/src/012-protocolos_red/network_architecture/virtual_networks/vbox/local_in_global_out.md)). 
5. Sólo nos queda comprobar si funciona. Desde el explorador de archivos de Windows o desde cualquier navegador podemos acceder tecleando en la barra de direcciones `ftp://192.168.1.12` (cambia la dirección por la tuya).

### Windows 7+ con FileZilla
1. Descarga el servidor desde [aquí](https://filezilla-project.org/download.php?type=server) e instálalo. Si tienes un servidor FTP ya corriendo, desactívalo.
2. Ejecuta el administrador. Si te aparece el mensaje `Could not load TLS libraries. Aborting start of administration interface.` debes actualizar bibliotecas, las puedes encontrar [aquí](https://rootlayer.net/billing/index.php/knowledgebase/6/How-to-fix-Could-not-load-TLS-libraries-Filezilla-Server-related-Error.html). Descarga el archivo de tu versión de Windows y ejecútalo.
3. Abre el panel de control de FileZilla server y edita la configuración en `Edit` -> `Settings` y `Edit` -> `Users`, luego conecta el servidor y comprueba que está funcionando con cualquier cliente FTP, el sistema de archivos de Windows o un navegador web mediante la dirección `ftp://localhost` (desde la misma máquina).
