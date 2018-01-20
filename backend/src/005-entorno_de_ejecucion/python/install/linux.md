## Instalación de Python en Linux

1. Asegurarnos de que tenemos los paquetes necesarios. Los siguientes comandos depende de tu distribución, aquí se proveen los necesarios para derivados de Debian:
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev
sudo apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
sudo apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev
```

2. [Buscar aquí](https://www.python.org/ftp/python/) el número de versión (dentro de su carpeta) y el patch que queremos.
3. Ejecutar el los siguientes comandos dependiendo del número de versión:

```
wget https://www.python.org/ftp/python/<NUMERO.DE.VERSIÓN>/<nombre_del_archivo_comprimido_con_patch>.tgz
tar xvf <nombre_del_archivo_comprimido_con_patch>
cd <nombre_del_archivo_comprimido_con_patch>
./configure --enable-optimizations
make -j8
sudo make altinstall
```

> La instalación con `sudo make altinstall` permite tener las diferentes versiones de Python con acceso al binario diferente por versión. Así podemos ejecutar `python2.7`, `python3.4`, `python3.7`... etc.

4. Comprobar que está instalando ejecutando el binario de nuestra versión.