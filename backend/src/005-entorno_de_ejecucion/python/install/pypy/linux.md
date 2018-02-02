## Instalación de Pypy en Linux

#### [Distribuciones binarias portables](https://github.com/squeaky-pl/portable-pypy#portable-pypy-distribution-for-linux)

### Instalar versión 3.5 en arquitectura x86_64
```
sudo apt-get install wget
wget https://bitbucket.org/squeaky/portable-pypy/downloads/pypy3.5-5.10.1-linux_x86_64-portable.tar.bz2
tar xvf pypy3.5-5.10.1-linux_x86_64-portable.tar.bz2
rm pypy3.5-5.10.1-linux_x86_64-portable.tar.bz2
sudo mv pypy3.5-5.10.1-linux_x86_64-portable /usr/lib/pypy3.5
sudo ln -s /usr/lib/pypy3.5/bin/pypy3.5 /usr/bin/pypy3.5
```

### Instalar versión 2.7 mediante gestor de paquetes
```
sudo apt-get install pypy   # (Debian/Ubuntu)
sudo mv /usr/bin/pypy /usr/bin/pypy2.7
```
