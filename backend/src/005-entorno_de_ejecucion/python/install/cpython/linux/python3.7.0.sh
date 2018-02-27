#!/bin/sh

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0a4.tar.xz
tar xvf Python-3.7.0a4.tar.xz
rm Python-3.7.0a4.tar.xz
cd Python-3.7.0a4
./configure --enable-optimizations --enable-ipv6
make -j8
sudo make altinstall
cd ..
rm -rf Python-3.7.0a4
