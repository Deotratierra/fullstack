## Hola mundo en Cassandra

1. Creamos un espacio de claves (keyspace): `CREATE KEYSPACE alvaro WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': 1 };`. Este comando nos creará el espacio de clave `alvaro`.
2. Vemos todos los espacios de claves: `DESC KEYSPACES;`
3. Activamos el espacio de claves que acabamos de crear: `USE alvaro;`
4. Creamos una tabla dentro del espacio: `CREATE TABLE users (firstname text, lastname text, email text, organization text, PRIMARY KEY (lastname));`
5. Obtenemos más información de la tabla que hemos creado: `DESC SCHEMA;`
6. Insertamos un usuario en la tabla: `INSERT INTO users (firstname, lastname, email, organization) VALUES ('Álvaro', 'Mondéjar', 'mondejar1994@gmail.com', 'Siglo25');`
7. Mostramos todos los usuarios de la tabla: `SELECT * FROM users;`

