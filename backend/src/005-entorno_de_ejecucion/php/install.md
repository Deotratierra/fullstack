## Instalación de PHP

### 7.2.6 en Debian 9
Este tutorial explica como instalar la versión 7.2.6 de PHP en Debian 9. Sólo hay que ejecutar los siguientes comandos:

```
sudo apt install apt-transport-https lsb-release ca-certificates
sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
sudo sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list'
sudo apt update
sudo apt install nginx php7.2 php7.2-common php7.2-cli php7.2-fpm php7.2-mysql php7.2-xml php7.2-curl php7.2-mbstring php7.2-zip
```

Para comprobar que está instalado ejecutamos: `php -v`

_________________________________________
