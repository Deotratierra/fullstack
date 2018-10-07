"use strict"

var gulp = require("gulp"),
    concat = require("gulp-concat"),  // npm install gulp-concat
    uglify = require("gulp-uglify");  // npm install gulp-uglify

// Creamos una tarea de nombre build
gulp.task("build", function() {
    gulp.src("src/*.js")  // Tomamos unos archivos fuente
        .pipe(concat("bundle.js"))  // Los concatenamos en un archivo de salida
        .pipe(uglify())   // Los minificamos
        .pipe(gulp.dest("build/")) // Le añadimos la carpeta de destino
});

// Para lanzarlo ejecutamos gulp junto al nombre de la tarea, en este caso:
// gulp build

// En la carpeta build/ ya tendremos nuestros archivos concatenados
// y el archivo resultante minificado

