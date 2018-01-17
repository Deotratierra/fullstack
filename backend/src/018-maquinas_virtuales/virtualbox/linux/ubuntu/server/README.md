## Ubuntu Server en VirtualBox

### Instalación
1. [Descarga la versión que quieras](https://www.ubuntu.com/download/server)
2. Configura la máquina virtual con Ubuntu 64 bits.
3. Ejecuta y sigue los pasos de instalación y ya estará operando.

### Conexión vía SSH
1. Desde dentro de la máquina ejecuta: `if config | grep "broadcast`. La dirección que aparece al lado de `inet` será la dirección IP privada dentro de tu red local. Quédate con ella.
2. Accede en la configuración de la máquina a `Red` -> `Avanzadas` -> `Reenvío de puertos`. Agrega una nueva regla de reenvío con las siguientes características:
    - Nombre: `SSH`
    - Protocolo: `TCP`
    - Ip anfitrión: `127.0.0.1`
    - Puerto anfitrión: `2222`
    - IP invitado: `<IP.del.primer.paso>`
    - Puerto invitado: `22`
3. Con esta regla de reenvío, estás indicando que todo lo que llegue al puerto `2222` de tu máquina anfitriona (`127.0.0.1`) será redireccionado al puerto `22` (SSH) de la máquina virtual por la IP que hayas configurado. Así que para loguearte ejecuta `ssh -p 2222 <tu_usuario_ubuntu_server>@<IP.del.primer.paso>`. [Puedes usar sshpass para pasar directamente tu contraseña en el comando](https://github.com/mondeja/fullstack/blob/master/backend/src/012-protocolos_red/SSH/SFTP_SCP/connect.sh).
