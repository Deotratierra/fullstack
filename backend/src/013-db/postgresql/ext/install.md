## Instalar extensiones para PostgreSQL

Para instalar extensiones en PostgreSQL tenemos que tener en cuenta dos aspectos: el primero es tener la extensión habilitada en nuestro servidor PostgreSQL y el segundo instalarla en una base de datos.

- Saber que extensiones tenemos habilitadas en nuestro servidor: `SELECT * FROM pg_available_extensions ORDER BY name;`
- Instalar una extensión en la base de datos que estamos usando (necesitamos privilegios de administrador): `CREATE EXTENSION <nombre_de_la_extensión>;`
- Mostrar las extensiones que tenemos instaladas en la base de datos: `SELECT name,default_version,installed_version,comment FROM pg_available_extensions WHERE installed_version IS NOT NULL ORDER BY name;`