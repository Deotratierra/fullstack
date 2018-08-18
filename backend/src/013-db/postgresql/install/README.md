## Instalación de PostgreSQL

### Instalación mínima en sistemas basados en Debian
Los sistemas basados en Debian contienen los paquetes para la instalación mínima de PostgreSQL:

- Instalar: `sudo apt-get install postgresql postgresql-contrib` ó indicando la versión `sudo apt-get install postgresql-9.6`
- Comprobar instalación:
  - `sudo systemctl start postgresql && sudo systemctl status postgresql`
  - `su - postgres`
  - `psql`


### Debian 9
- Instalar:
  ```
  wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
  sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
  sudo apt-get update
  sudo apt-get install postgresql postgresql-contrib
  ```



