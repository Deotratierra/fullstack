## Paquetes en Java

Un paquete de Java es un contenedor que agrupa tipos relacionados entre sí.

Por ejemplo, en el núcleo de Java la interfaz `ResultSet` pertenece al paquete `java.sql`. Ese paquete contiene todos los tipos necesarios para lanzar consultas SQL y realizar conexiones con bases de datos. Dentro de este paquete existe la clase `Date`, la cual permite trabajar con fechas en las consultas SQL. Sin embargo, dentro de los paquetes incluidos en el núcleo de Java, también existe la clase `Date`, que sirve para trabajar con fechas de manera general.

Para diferenciar el contexto de estas dos clases con el mismo nombre, estas se ubican en paquetes diferentes:

- `java.util.Date`: Clase normal de fecha que puede ser usada en cualquier lugar.
- `java.sql.Date`: Clase para fechas usadas en consultas SQL.

### ¿Cómo crear un paquete en Java?
Para definir un paquete en Java, usamos la palabra clave `package`, de la siguiente forma:

```java
package nombreDelPaquete;
```

Java usa los directorios del sistema para almacenar paquetes. Comprueba la estructura de directorios almacenada en esta carpeta. Dentro de `com/modulo`, hay un paquete llamado `com.modulo`, definido en el archivo `com/modulo/Modulo.java`.

Desde el archivo `Import.java`, importamos la clase definida en `com/modulo/Modulo.java` y ejecutamos la función `main`.

