## Roles en PostgreSQL

Por defecto, Postgress utiliza un concepto llamado "roles" que maneja identificación y autorización. Estos son, de algún modo, similares a los estilos de cuentas en Unix, pero Postgres no distingue entre usuarios y grupos y en su lugar prefiere ser más flexible con el término "rol".

Al instalar PostgreSQL, si intentamos acceder al intérprete de comandos desde nuestro usuario individual del sistema (no como superusuario) nos lanzará el error `psql: FATAL:  no existe el rol «nombre_de_usuario»`. 

El procedimiento de instalación creó a un usuario llamado postgres que está asociado con el rol Postgres por defecto. Para utilizar Postgres, podemos identificarnos con esa cuenta:

```bash
sudo -i -u postgres
```

Ahora podremos acceder a la consola Postgres inmediatamente escribiendo `psql`.

### Crear un nuevo usuario

Podemos crear un nuevo usuario de forma interactiva ejecutando `createuser --interactive` desde la terminal logueados como el usuario `postgres`. Luego añadimos el usuario al sistema con `sudo adduser <nombre_del_usuario>` (ver [Administración de usuarios en Linux](https://github.com/mondeja/fullstack/tree/master/backend/src/009-sistema_operativo/users)). Ahora podemos acceder al nuevo usuario dentro de la terminal con `sudo -i -u <nombre_del_usuario>`. 

> El nombre que le demos al nuevo usuario será enlazado a una base de datos del mismo nombre. Si esta base de datos no existe e intentamos acceder a la consola `psql` logueados como el nuevo usuario, nos lanzará el error `psql: FATAL:  no existe la base de datos «nombre_de_usuario»`, por lo que debemos crear antes la nueva base de datos con `createdb <nombre_del_usuario>` o especificar una base de datos a usar (ver [Administración de bases de datos](https://github.com/mondeja/fullstack/tree/master/backend/src/013-db/postgresql/tutoriales/db.md)).

- Ver todos los roles creados (desde `psql`): `\du`