## Administración de bases de datos con PostgreSQL

> Los siguientes comandos requieren estar logueados como un usuario administrador de PostgreSQL (ver [roles](https://github.com/mondeja/fullstack/tree/master/backend/src/013-db/postgresql/tutoriales/roles.md)): `sudo -i -u postgres`

- Crear una base de datos: `createdb <nombre_de_la_base_de_datos>`

De forma predeterminada, Postgres suopne que habrá una base de datos con el mismo nombre que el rol que se utiliza para iniciar la sesión, a la que el rol tiene acceso.

- Conectar un usuario a una base de datos diferente: `psql -d <nombre_de_la_base_de_datos>`

