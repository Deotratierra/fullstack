## Instalación de MySQL en Ubuntu
```
sudo apt-get update
sudo apt-get install mysql-server
mysql_secure_installation
```

El puerto por defecto para MySQL es `3306`.

___________________________________________________

## Comandos útiles en MySQL (local)

- Iniciar shell:
`mysql -u root -p`

> Pide la contraseña del usuario que establecimos como raíz al instalar. Para agregar más usuarios: https://dev.mysql.com/doc/refman/5.7/en/adding-users.html

- Cerrar shell:
`QUIT`

- Iniciar y apagar servidor (en Ubuntu):
`sudo /etc/init.d/mysql start`
`sudo /etc/init.d/mysql stop`

### Manejo básico de bases de datos:

- Mostrar las bases de datos:
`SHOW DATABASES;`

- Crear una base de datos:
`CREATE DATABASE <database_name>;`

- Usar una base de datos
`USE <database_name>`

- Mostrar las tablas de una base de datos:
`SHOW TABLES;`

- Crear una tabla:
```
CREATE TABLE cats
(
  id              INT unsigned NOT NULL AUTO_INCREMENT,
  name            VARCHAR(150) NOT NULL,                
  owner           VARCHAR(150) NOT NULL,                
  birth           DATE NOT NULL,                        
  PRIMARY KEY     (id)                                  
);
```
- Mostrar información de las columnas de una tabla:
`DESCRIBE cats;`

- Insertar un registro en una tabla:
```
INSERT INTO cats ( name, owner, birth) VALUES
  ( 'Sandy', 'Lennon', '2015-01-03' ),
  ( 'Cookie', 'Casey', '2013-11-13' ),
  ( 'Charlie', 'River', '2016-05-21' );
```
- Mostrar los registros de una tabla:
`SELECT * FROM cats;`

- Borrar un registro de una tabla:
`DELETE FROM cats WHERE name='Cookie';`

- Agregar columna a una tabla:
`ALTER TABLE cats ADD gender CHAR(1) AFTER name;`

- Borrar columna de una tabla:
`ALTER TABLE cats DROP gender;`



>Fuente: https://dev.mysql.com/doc/mysql-getting-started/en/

