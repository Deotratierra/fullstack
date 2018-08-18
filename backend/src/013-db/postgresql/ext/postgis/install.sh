#!/usr/bin/env bash

echo "Installing dependencies..."
sudo apt-get install wget git g++ autoconf automake libtoool postgresql-server-dev-10

echo "Building Geos-3.7.0beta2 ..."
wget http://download.osgeo.org/geos/geos-3.7.0beta2.tar.bz2
tar -xvf geos-3.7.0beta2.tar.bz2
rm geos-3.7.0beta2.tar.bz2
cd geos-3.7.0beta2
./configure
make
sudo make install
cd ..
rm -rf geos-3.7.0beta2

echo "Installing LibXML2 ..."
sudo apt-get install libxml2-dev

echo "Building Proj-4.9.1 ..."
wget http://download.osgeo.org/proj/proj-4.9.1.tar.gz
tar -xvf proj-4.9.1.tar.gz
rm proj-4.9.1.tar.gz
cd proj-4.9.1
./configure
make
sudo make install
cd ..
rm -rf proj-4.9.1

echo "Building GDAL-2.3.1 ..."
wget https://download.osgeo.org/gdal/2.3.1/gdal-2.3.1.tar.gz
tar -xvf gdal-2.3.1.tar.gz
rm gdal-2.3.1.tar.gz
cd gdal-2.3.1
./configure
make
sudo make install
cd ..
rm -rf gdal-2.3.1

echo "Building JSON-C ..."
git clone https://github.com/json-c/json-c.git
cd json-c
sh autogen.sh
./configure
make
make install
cd ..
rm -rf json-c

echo "Building PostGIS-2.4.4 ..."
wget https://download.osgeo.org/postgis/source/postgis-2.4.4.tar.gz
tar -xvf postgis-2.4.4.tar.gz
rm postgis-2.4.4.tar.gz
cd postgis-2.4.4
./configure
make
sudo make install
