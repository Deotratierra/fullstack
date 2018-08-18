## Espacios de claves en Cassandra (Keyspaces)

Son los contenedores para datos más exteriores en Cassandra. Todos los datos deben vivir dentro de un keyspace. En el caso de Cassandra es una **colección de familias de columnas**.

Una familia de columnas es una colección de filas y cada fila es una colección de columnas. Las familias de columnas son definidas, pero no es necesario para cada fila tener todasd las columnas y las columnas pueden ser agregadas o eliminadas de una fila como y cuando se requiera.

Una **columna** es la unidad básica de datos en Cassandra. Tiene 3 valores: **llave** o nombre de la columna, **valor de columna** y una **estampa de tiempo**.

Una **super columna** es un tipo especial de columna que almacena un mapa de otras sub-columnas. Esto posibilita el almacenamiento de datos más complejos más fácil y también hace que la recuperación de datos sea más rápida ya que cada familia de columnas en Cassandra es almacenada en una sola fila en el sistema de archivos.

### Comandos
- Crear un keyspace: `CREATE KEYSPACE nombre WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};`
- Modificar un keyspace: `ALTER KEYSPACE nombre WITH REPLICATION = { 'class' : 'SimpleStrategy','replication_factor' : 3};`
- Eliminar un keyspace: `DROP KEYSPACE nombre;`
- Usar un keyspace: `USE nombre;`
- Mostrar el nombre de los keyspaces creados: `DESC KEYSPACES;`
- Mostrar información detallada sobre los keyspaces: `SELECT * FROM system_schema.keyspaces;`