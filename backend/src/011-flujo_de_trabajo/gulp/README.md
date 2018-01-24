## Tutorial de Gulp

#### Instalación global
`sudo npm i -g gulp`

Verificar que ha sido instalado: `gulp -v`

#### Instalación local
`npm i --save-dev gulp`

______________________________

### Funcionamiento
Gulp está basado en un sistema de tareas a base de tuberías utilizando la biblioteca [orchestator](https://github.com/robrich/orchestrator) y la biblioteca [vinyl-fs](https://github.com/wearefractal/vinyl-fs) para escribir streams.

Para configurar la ejecución de las tareas creamos un archivo llamado `gulpfile.js`. [Aquí puedes ver](https://github.com/mondeja/fullstack/blob/master/backend/src/037-automatizar_tareas/gulp/hola_mundo/gulpfile.js) un ejemplo básico de configuración.

### Comandos principales
Con el método `gulp.task()` definimos una tarea. Este toma 3 argumentos: el nmbre de la tarea, la o las tareas de las que depende esta y la función que se llamará al ejecutarla.

Para ejecutar una tarea: `gulp <nombre_de_la_tearea>`

Una tarea puede llamar a otras tareas, por ejemplo:
```
gulp.task("desayunar", ["calentar_leche", "tostar_pan"]);
```
Cuando ejecutamos `gulp desayunar` se calentará la leche y se tostará el pan, todo de forma asíncrona.

#### Tareas por defecto:
Si queremos que una tarea corra ejecutando tan sólo la palabra `gulp`, llamamos a la tarea `"default"`.

#### Archivos fuente:
Con la función `gulp.src(<path>)`, cada vez que gulp encuentre un archivo que coincida con el patrón, lo irá metiendo en un stream, que será una colección de archivos. Gulp utiliza la biblioteca [node-glob](https://github.com/isaacs/node-glob) para obtener los archivos, y esta a su vez utiliza la sintaxis de [minimatch](https://github.com/isaacs/minimatch), una biblioteca de expresiones regulares.

#### Tuberías
El método `.pipe()` es un método de NodeJS para manejar streams. Es el método que va enlazando las tareas.

#### Destino
La función `gulp.dest()` indica la o las carpetas donde serán escritos los datos y devuelve el canal, por si deseamos realizar más acciones.

#### Observar archivos
El método `gulp.watch()` observa archivos y ejecuta tareas cuando se modifican. Hay dos formas de usarlo:
- `gulp.watch(glob, tareas)`
- `gulp.watch(glob, callback)`

> Fuentes:
> https://frontendlabs.io/1669--gulp-js-en-espanol-tutorial-basico-primeros-pasos-y-ejemplos
> https://frontendlabs.io/1752--gulp-js-plugins-como-configurar-tareas


______________________________

### Plugins
Podemos buscar plugins desde [la página oficial de GulpJS](https://gulpjs.com/plugins/).

- [`gulp-concat`](https://www.npmjs.com/package/gulp-concat): Concatenar archivos.
- [`gulp-uglify`](https://www.npmjs.com/package/gulp-uglify): Minificar archivos javascript.
- [`gulp-babel`](https://www.npmjs.com/package/gulp-babel): Transpilador de código (React, ES6...). También necesitamos `babel-core` y `babel-register`. 
    Presets:
    + `npm install --save-dev babel-preset-es2015`
    + `npm install --save-dev babel-preset-react`
- [`browserify`](http://browserify.org/index.html): Convierte los `require` de Javascript a magia en importaciones para que trabajen con el navegador.
- [`gulp-clean-css`](https://www.npmjs.com/package/gulp-clean-css): Minificar archivos `css` con [clean-css](https://github.com/jakubpawlowicz/clean-css).
- [`gulp-imagemin`](https://www.npmjs.com/package/gulp-imagemin): Minificar imágenes `png`, `jpeg`, `gif` y `svg`.
- [`gulp-jshint`](https://www.npmjs.com/package/gulp-jshint): Validación de sintaxis Javascript.
- [`gulp-rename`](https://www.npmjs.com/package/gulp-rename): Renombrar archivos.
- [`gulp-notify`](https://www.npmjs.com/package/gulp-notify): Notificación de errores, archivos...
- [`gulp-sass`](https://www.npmjs.com/package/gulp-sass): Transpilar archivos `scss` a `css`.
- [`gulp-jade`](https://www.npmjs.com/package/gulp-jade): Transpilar archivos `jade` a `html`.
- [`pump`](https://www.npmjs.com/package/pump): Cazar errores en los pipelines [sin hackear el código](https://github.com/terinjokes/gulp-uglify/blob/master/docs/why-use-pump/README.md#why-use-pump).
- [`gulp-if`](https://www.npmjs.com/package/gulp-if): Controlar condicionalmente el flujo de ejecución de las teareas.
- [`gulp-rimraf`](https://www.npmjs.com/package/gulp-rimraf): Eliminar archivos, directorios...

__________________________________

### Ejemplos

- [Minificar y concatenar archivos con `gulp-uglify` y `gulp-concat`](https://github.com/mondeja/fullstack/tree/master/backend/src/011-flujo_de_trabajo/gulp/hola_mundo/) (Hola mundo)
- [Transpilación de Javascript ES6 a ES5 con `gulp-babel`](https://github.com/mondeja/fullstack/tree/master/backend/src/011-flujo_de_trabajo/gulp/babel_es6_es5/gulpfile.babel.js)
- [Transpilación SCSS a CSS con `gulp-sass`](https://github.com/mondeja/fullstack/tree/master/backend/src/011-flujo_de_trabajo/gulp/sass_css/gulpfile.js)
- [Transpilación de Jade a HTML con `gulp-jade`](https://github.com/mondeja/fullstack/tree/master/backend/src/011-flujo_de_trabajo/gulp/jade_html/gulpfile.js)
- [Browserificación (modularizar Javascript en cliente) con `browserify`](https://github.com/mondeja/fullstack/tree/master/backend/src/011-flujo_de_trabajo/gulp/browserify/gulpfile.js)
