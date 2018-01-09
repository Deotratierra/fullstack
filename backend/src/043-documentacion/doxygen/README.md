## [Doxygen](https://es.wikipedia.org/wiki/Doxygen)
Generador de documentación para C++, C, Java, Objective-C, Python, IDL (versiones Corba y Microsoft), VHDL y en cierta medida para PHP, C# y D.

### Documentar
Los siguientes comandos se introducen en los comentarios antes de funciones, variables o bibliotecas para documentar el código:
- `@brief`: Indica que lo que sigue a continuación es el resumen de la función/clase/estrucura/enumerado/etc documentado.
- `@param`: Parámetro de una función. Debe estar seguido del nombre de la variable a la que nos referimos: `@param <variable> <explicación>`
- `@return`: Lo que retorna la función
- `@note`: Anotación.
- `@see`: Referencia a una función.

> [Aquí puedes consutar una lista](http://www.stack.nl/%7Edimitri/doxygen/manual/commands.html) con todos los comandos disponibles con su documentación.

### Comandos
- Crear el archivo de configuración del proyecto: `doxygen -g`
- Generar la documentación: `doxygen`