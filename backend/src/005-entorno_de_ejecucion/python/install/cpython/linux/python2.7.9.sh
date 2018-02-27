#!/bin/sh


wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9rc1.tgz
tar xvf Python-2.7.9rc1.tgz
rm Python-2.7.9rc1.tgz
cd Python-2.7.9rc1
./configure --enable-optimizations --enable-ipv6
make -j8
sudo make altinstall
cd ..
rm -rf Python-2.7.9rc1

echo "Python-2.7.9rc1 se ha instalado correctamente."