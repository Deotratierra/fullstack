# Logging en Linux
Linux posee un interesante sistema de logging. Los registros de los logs de los programas se guardan en el directorio `/var/log`. En cada mensaje aparece la fuente (programa que generó el mensaje), el nivel, la fecha y la hora.

## Comandos
### Monitorizar logs
- Monitorizar el contenido de un archivo: `tail -f <archivo>`

> Con el comando `tail` imprimimos las 10 últimas líneas de un archivo, pero si le añadimos la opción `-f`, seguirá el comando activo imprimiendo las nuevas líneas escritas en el archivo. Con el comando `tail -f /var/log/messages` monitorizamos los logs del sistema con niveles `info`, `notice` y `warn`.

### Registrar mensajes
- Enviar un log a un archivo: `logger -t mi_programa -f /var/log/messages "Mensaje ejemplo"`
- Enviar un log al demonio: `logger "<mensaje>"`

> El comando logger permite enviar eventos al demonio `syslogd`, por lo que se utiliza en scripts para registrar mensajes vía `sysklogd`. [Desde aquí](http://man7.org/linux/man-pages/man1/logger.1.html) podemos acceder a sus opciones.

___________________________________________

## Funcionamiento

### Niveles de prioridad
- `debug`
- `info`
- `notice`
- `warning`
- `warn`
- `err`
- `error`
- `crit`
- `alert`
- `emerg`
- `panic`

### Demonios
El sistema de logs arranca con el script `/etc/init.d/sysklogd`, y consta de dos demonios:
- `syslogd`: Gestiona los logs del sistema. Distribuye los mensajes a archivos, tuberías, destinos remotos, terminales o usuarios, usando las indicaciones del archivo de configuración `/etc/syslog.conf`, donde se indica qué se loguea y adonde se envían los logs.
- `klogd`: Se encarga de los logs del kernel. Lo normal es que `klogd` envíe sus mensajes a `syslogd` pero no siempre es así, sobre todo en los eventos de alta prioridad, que aparecen directamente por pantalla.

### Almacenamiento de logs
Los logs del sistema se guardan en `/var/log`, aunque muchos programas manejan sus propios logs y los guardan en `/var/log/<programa>`. También es posible especificar múltiples destinos para los mensajes. Algunos de los logs más importantes son:
    - `/var/log/messages`: Lo que llegan con nivel `info`, `notice` o `warn`.
    - `/var/log/kern.log`: Logs del kernel, generados por `klogd`.
    - `/var/log/auth.log`: Logins del sistema, activación de superusuario, etc.
    - `/var/log/dmesg`: Información que genera el kernel durante el arranque del sistema. Podemos ver su contenido con el comando `sudo dmesg`.

### Rotación de logs
Para solucionar el problema de una gran cantidad de almacenamiento de logs, Linux posee un script diario ubicado en `/etc/cron.daily` llamado `/etc/cron.daily/logrotate` que, como su nombre indica, se encarga de realizar una rotación de logs.

Lo que hace es comprimirlos y aplicar una rotación de archivos, dándoles la extensión `.1.gz`, `.2.gz`, etc. Por ejemplo, para el archivo `/var/log/messages`, podemos ver los archivos `messages.1.gz`, `messages.2.gz`, etc. Cuanto mayor sea el número más antiguo es el log. Cada día vuelve a crear un archivo vacío nuevo donde almacena los logs de hoy.

_________________________________________

## Configuración

### Enviar todos los logs a un archivo
Así podemos ver en tiempo real todo lo que pasa en nuestra máquina. Esto nos permitirá aprender más sobre nuestro sistema y cómo funciona, y también detectar cualquier anomalía o error que de otra manera pasarían desapercibidos. Para ello:
1. Creamos el archivo vacío `/var/log/all.log`: `sudo touch /var/log/all.log`
2. Añadimos al archivo `/etc/rsyslog.conf` la línea: `*.*       /var/log/all.log`
3. Volvemos a cargar la configuración del script `rsysklogd`: `sudo /etc/init.d/rsyslog restart`
4. Añadimos al archivo `/etc/logrotate.d/rsyslog` la línea: `/var/log/all.log`

Ya podemos monitorizar el sistema usando el comando: `tail -f /var/log/all.log`
Para comprobar que funciona enviamos un log al archivo `/var/log/messages` con el comando: `sudo logger -t mi_programa -f /var/log/messages "Mensaje ejemplo"`

> Fuentes:
> - http://www.estrellateyarde.org/logs-en-linux
> - http://proyectosbeta.net/2016/04/como-enviar-todos-los-logs-a-un-archivo-en-debian-jessie/
> - http://man7.org/linux/man-pages/man1/logger.1.html
