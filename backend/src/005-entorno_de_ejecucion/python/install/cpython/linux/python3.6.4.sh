#!/bin/sh

#wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
#tar xvf Python-3.6.4.tar.xz
sudo rm Python-3.6.4.tar.xz
cd Python-3.6.4
./configure --enable-optimizations --enable-ipv6
make -j8
sudo make altinstall
cd ..
rm -rf Python-3.6.4

echo "Python-3.6.4 se ha instalado correctamente."