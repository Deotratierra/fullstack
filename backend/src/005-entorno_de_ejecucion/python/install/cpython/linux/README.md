## Instalación de Python en Linux

1. Asegurarnos de que tenemos los paquetes necesarios. Los siguientes comandos dependen de tu distribución, aquí se proveen los necesarios para derivados de Debian y derivados:
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncurses5-dev  libncursesw5-dev xz-utils tk-dev
```

2. [Buscar aquí](https://www.python.org/ftp/python/) el número de versión (dentro de su carpeta) y el patch que queremos.
3. Ejecutar el los siguientes comandos dependiendo del número de versión:

```
wget https://www.python.org/ftp/python/<NUMERO.DE.VERSIÓN>/<nombre_del_archivo_comprimido_con_patch>.tgz
tar xvf <nombre_del_archivo_comprimido_con_patch>
cd <nombre_del_archivo_comprimido_con_patch>
./configure --enable-optimizations --enable-ipv6
make -j8
sudo make altinstall
```

> La instalación con `sudo make altinstall` permite tener las diferentes versiones de Python con acceso al binario diferente por versión. Así podemos ejecutar `python2.7`, `python3.4`, `python3.7`... etc. Los binarios se guardan por defecto en `/usr/bin`.

4. Comprobar que está instalando ejecutando el binario de nuestra versión.
5. Salir del directorio `cd ..` y borrar el directorio que descargamos: `rm -Rf <nombre_del_archivo_comprimido_con_patch>`
