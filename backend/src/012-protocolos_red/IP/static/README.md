# Configurar IP estática

## Linux
Si tenemos la opción de editar la configuración de red desde una la interfaz gráfica de nuestra distribución, es preferible hacerlo desde allí, pero si no hay que seguir los siguientes pasos, según distribución:

### Debian/Ubuntu
> Ubuntu Server tiene una configuración diferente, que yo sepa.

Para las distribuciones basadas en Debian, debemos modificar el archivo `/etc/network/interfaces`. Por defecto aparecen las siguientes líneas:
```
auto lo
iface lo inet loopback
```

Hay que cambiar ese código algo como esto:
```
auto eth1
iface eth1 inet static
address 192.168.1.11
netmask 255.255.255.0
```

Luego debes reiniciar la red ejecutando: `sudo /etc/init.d/networking restart`. Si da error, ve abajo al apartado `En caso de error al reiniciar la red`.

Si estás conectado a la red vía cable de red la clave lo más seguro es que tu clave sea `eth0` o `eth1`. En la línea `address` yo he colocado `192.168.1.11` pero tu puedes colocar la IP privada que quieras, siempre que siga las reglas de la IP privadas según tu [máscara de subred](https://github.com/mondeja/fullstack/tree/master/backend/src/012-protocolos_red/IP/subnet_masks).

Si tienes dudas acerca de esto ve colocando `192.168.1.10` y ve aumentando el último número si necesitas conectar más ordenadores, procurando que dos no tengan la misma IP.

________________________

## Windows

### Windows7
Vamos a `Panel de Control` -> `Redes e Internet` -> `Centro de redes y recursos compartidos` -> `Cambiar configuración del adaptador`. Allí hacemos click con el botón secundario del ratón a la red que queremos conectarnos y seleccionamos `Propiedades` -> `Protocolo de internet versión 4 (TCP/IPv4)` (doble click) y establecemos la dirección IP, máscara de subred y puerta de enlace predeterminada.

Una configuración de ejemplo podría ser:
- Dirección IP: `192.168.1.12`
- Máscara de subred: `255.255.255.0`
- Puerta de enlace predeterminada: `192.168.1.1`
