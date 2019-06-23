## Compilación de módulos Java

En Java, hay una norma: debemos hacer coincidir el nombre del archivo y el nombre de la clase que expone el mismo (tanto en mayúsculas como en minúsculas). En el ejemplo de este directorio, podemos ver que el nombre del archivo es `Module.java` y el nombre de la clase que expone es `Module`.

Para compilar, ejecutamos el binario `javac` indicando el nombre del archivo que queremos compilar. Eso nos generará un archivo con la extensión `.class`, que es el bytecode que será capaz de leer la máquina virtual de Java. Siguiendo el ejemplo de este directorio ejecutamos `javac Module.java` y se nos creará el archivo `Module.class`.

Para ejecutar el módulo, ejecutamos `java` seguido del nombre de la clase expuesta en el mismo:

```
$ java Module
¡Hola mundo desde Java!
```
