## Sistemas de gestión de paquetes en Lnux

### Apt - Debian
En los sistemas basados Debian debemos configurar links que hacen referencia a archivos del sistema operativo, los cuales configuran las actualizaciones del núcleo y los programas. Estas cabeceras se encuentran en el archivo `/etc/apt/sources.list`, pero también podemos añadir nuevos archivos con extensión `.list` al directorio `/etc/apt/sources.list.d/` y serán leídas.

Dependiendo de la versión que estemos usando, debemos definir unas cabeceras distintas en este archivo:
- Debian 8 (Jessie):
  ```
  deb http://httpredir.debian.org/debian jessie main
  deb http://httpredir.debian.org/debian jessie-updates main
  deb http://security.debian.org jessie/updates main
  ```
- Debian 9 (Stretch)
  ```
  deb http://httpredir.debian.org/debian stretch main
  deb http://httpredir.debian.org/debian stretch-updates main
  deb http://security.debian.org/debian stretch/updates main
  ```

#### Actualizar Debian 8 a 9
```bash
su
apt-get update
apt-get upgrade
apt-get dist-upgrade

apt-get update
apt-get upgrade
```

#### Problemas comunes

##### Error `Cambio de medio...`
```
Cambio de medio: Inserte el disco etiquetado como <<Debian ...>> en la unidad <</media/cdrom>> y pule Intro.
```

Al instalar Debian, si no hemos configurado la red durante el proceso de instalación, las cabeceras APT que se configuran en `/etc/apt/sources.list` hacen referencia a una instalación desde un CD. Supongo que es más cómodo para los desarrolladores trabajar con CDs pero yo uso `.iso` que me parece lo más cómodo.

Así que la solucion es eliminar las líneas que hacen referencia al medio `cdrom` en el archivo `/etc/apt/sources.list`.

