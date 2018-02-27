#!/bin/sh

wget https://www.python.org/ftp/python/3.5.5/Python-3.5.5rc1.tar.xz
tar xvf Python-3.5.5rc1.tar.xz
rm Python-3.5.5rc1.tar.xz
cd Python-3.5.5rc1
./configure --enable-optimizations --enable-ipv6
make -j8
sudo make altinstall
cd ..
rm -rf Python-3.5.5rc1

echo "Python-3.5.5rc1 se ha instalado correctamente."