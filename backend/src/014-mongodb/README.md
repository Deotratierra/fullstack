## Comandos útiles en MongoDB (local)

- Inicializar (puerto 27017):
`mongod`

- Inicializar en otro puerto:
`mongod --port 8765`

_____________________________________

- Iniciar shell:
`mongo`

- Cerrar shell:
`exit`

- Mostrar las bases de datos:
`show dbs`

- Crear una nueva o cambiar a una base de datos existente:
`use <database_name>`

- Insertar un campo en una colección:
`db.<collection_name>.insert( {"foo": "bar"} )`

- Borrar una base de datos:
`db.dropDatabase()`


