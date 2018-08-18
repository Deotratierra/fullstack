## Instalación de PostGIS
La forma más fácil de instalar PostGIS en equipos Linux es compilar el código fuente, que es la cual veremos aquí.

> Si estás en Ubuntu, [CartoDB ofrece repositorios PPA listos para instalar PostGIS de forma más fácil](http://cartodb.readthedocs.io/en/latest/install.html#postgresql).

### Requisitos
Necesitamos tener instalado PostgreSQL con las extensiones como `postgresql-server-dev`, las cuales vienen incluidas en equipos basados en Debian dentro del paquete `postgresql-contrib` (ver [Instalación de PostgreSQL](https://github.com/mondeja/fullstack/tree/master/backend/src/013-db/postgresql/install)).

Podemos seguir [este tutorial (Debian 9)](https://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS24Debian9src) o compilar el código fuente de todas las dependencias como se explica a continuación.

Antes de compilar PostGIS, necesitamos instalar las siguientes dependencias:
- [GEOS](https://trac.osgeo.org/geos): `sudo apt-get install libgeos++`. Para acceder a todas las características de PostGIS hay que instalar la última versión disponible [desde aquí](https://trac.osgeo.org/geos/) y compilar el código fuente:
  ```bash
  ./configure
  make
  make install
  ```
- [Libxml2](http://xmlsoft.org/): `sudo apt-get install libxml2-dev`
- [Proj4](https://proj4.org/): 
  ```bash
  wget http://download.osgeo.org/proj/proj-4.9.1.tar.gz
  tar -xvf proj-4.9.1.tar.gz
  rm proj-4.9.1.tar.gz
  cd proj-4.9.1
  ./configure
  make
  make install
  cd ..
  rm -rf proj-4.9.1
  ```
- [GDAL](https://gdal.org/):
  ```bash
  sudo apt-get install g++
  wget https://download.osgeo.org/gdal/2.3.1/gdal-2.3.1.tar.gz
  tar -xvf gdal-2.3.1.tar.gz
  rm gdal-2.3.1.tar.gz
  cd gdal-2.3.1
  ./configure
  make
  make install
  cd ..
  rm -rf gdal-2.3.1
  ```
- [JSON-C](https://github.com/json-c/json-c):
  ```bash
  sudo apt-get install autoconf automake libtoool
  git clone https://github.com/json-c/json-c.git
  cd json-c
  sh autogen.sh
  ./configure
  make
  make install
  cd ..
  rm -rf json-c
  ```

> Para más información sobre como instalar en diferentes sistemas operativos o incluir dependencias adicionales como Protobuf [ir aquí](https://trac.osgeo.org/postgis/wiki/UsersWikiInstall).

### Comprobar la instalación y configurar PostGIS

- Primero comprobamos que tenemos todas las bibliotecas necesarias instaladas:
  ```bash
  pg_config --version    # Versión de PostgreSQL
  geos-config --version  # Version de GEOS
  gdal-config --version  # Versión de GDAL
  proj                   # Versión de Proj
  ```

- Luego reiniciamos el servicio PostgreSQL (si esta iniciado, si no lo lanzaríamos con `start`):
  ```bash
  sudo service postgresql status
  sudo service postgresql restart
  ```
- Lo siguiente será comprobar que la extensión `postgis` está disponible en nuestra base de datos `postgres`. Desde la consola `psql` con un usuario postgres administrador ejecutamos:
  ```bash
  SELECT * FROM pg_available_extensions ORDER BY name;
  ```
  Si aparece `postgis` quiere decir que ya podemos instalar las extensiones en la base de datos:
  ```bash
  CREATE EXTENSION postgis;
  CREATE EXTENSION postgis_topology;
  ```
  Para comprobar que han sido instalada correctamente ejecutamos:
  ```bash
  SELECT name,default_version,installed_version,comment FROM pg_available_extensions WHERE installed_version IS NOT NULL ORDER BY name;
  ```
  > También podemos consultar las versiones instaladas ejecutando `SELECT PostGIS_full_version();`
