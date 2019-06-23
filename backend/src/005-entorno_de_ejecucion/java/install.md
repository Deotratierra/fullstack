## Instalar entorno de desarollo Java

### Debian 9
```bash
sudo apt-get install default-jre
sudo apt-get install default-jdk
```

> Comprobamos si tenemos Java instalado ejecutando: `java -version`
> Comprobamos si tenemos el compilador de java instalado: `javac -version`

Deberíamos obtener una salida similar a esta:
```
java version "1.8.0_131"
Java(TM) SE Runtime Environment (build 1.8.0_131-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.131-b11, mixed mode)
```

Si no está instalado:
```bash
apt-get install software-properties-common dirmngr
add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu yakkety main"
apt update
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886
apt-get install oracle-java8-installer
```

__________________________

