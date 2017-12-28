## Browserify
Con esta herramienta podemos crear el frontend de la aplicación de forma modular usando `require()` y luego empaquetar nuestros módulos en un archivo javascript que pueda ser usado en el navegador.

### Instalación
`npm i -g browserify`

### Configuración
Para usarla podemos hacerlo a través de `gulp`. En la web hay muchos tutoriales de cómo hacerlo, pero la gran mayoría sólo incluyen ejemplos en los cuales todos los archivos empaquetados van a parar a un gran archivo central `.js`. Para un entorno de producción esto implica cargar desde diferentes partes de nuestra web código innecesario.

Para solucionarlo podemos crear varios bundles y así tendremos el código modularizado, reduciendo los tiempos de carga y organizándolo todo mejor. En el archivo [`gulpfile.js`](gulpfile.js) de este directorio hay un ejemplo de cómo hacerlo.

>Fuentes:
- https://github.com/gulpjs/gulp/tree/master/docs/recipes