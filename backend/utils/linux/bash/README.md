## Comandos útiles en Bash (Ubuntu/Debian)

### Ejecución
- Lanzar un programa en segundo plano: 
```bash
screen
<comando_a_ejecutar>
Ctrl+A, D
```
- Volver al programa: `screen -rD`
> Si hay varias pantallas guardadas ejecutamos `screen -rD` y luego seleccionamos el número que aparece antes de ".pts" con el comando:`screen -xr <número>`

### Configuración
- Configurar la consola: `sudo nano /etc/bash.bashrc`
- Editar alias: `sudo nano /etc/bash.bashrc`

### Networking
- Reiniciar la red: `sudo /etc/init.d/networking restart`
- Puertos en escucha: `netstat -tln`

### Información del sistema
- Espacio en discos: `df -h`
- Número de CPUs: `cat /proc/cpuinfo | grep processor | wc -l`

