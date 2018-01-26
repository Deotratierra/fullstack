'use strict';

/* Ejecutar mediante una de las siguientes instrucciones:
gulp
gulp sass
*/

var gulp = require('gulp');       // npm i --save-dev gulp
var sass = require('gulp-sass');  // npm i --save-dev gulp-sass

// Creamos una tarea de gulp con el nombre "sass"
gulp.task("sass", function () {
  return gulp.src("*.scss")  // Obtenemos todos los archivos con extensión .scss
    // de forma recursiva por todos los subdirectorios bajo el actual
    .pipe(sass().on("error", sass.logError)) // Si hay un error avisa
    .pipe(gulp.dest("."));   // El destino de los archivos .css resultantes
                             // es la carpeta actual
});

// Si se produce un cambio en los archivos .scss
gulp.task("watch", function() {
  gulp.watch("*.scss", ["sass"]);  // vuelve a ejecutar la tarea "sass"
});

// Tarea a ejecutar con el comando: gulp
gulp.task("default", ["watch"]);  // Empieza a mirar los cambios en los archivos .scss
