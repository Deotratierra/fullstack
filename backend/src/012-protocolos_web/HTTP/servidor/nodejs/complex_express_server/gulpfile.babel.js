"use strict";

import gulp from "gulp";
import babel from "gulp-babel";
import jshint from "gulp-jshint";
import uglify from "gulp-uglify";
import cleanCSS from "gulp-clean-css";
import jade from "gulp-jade";
import sass from "gulp-sass";
import nodemon from "gulp-nodemon";

const dirs = {dest: "build"};

const debug = true,
      verbose = false;

let tasks = ["es6", "jade", "sass"];
if (debug){
  tasks.push("lint");
}

// ============================
// ====  ES6 compilation  =====

gulp.task("es6", () => {
    const stream = gulp.src("src/**/*.js")
        .pipe(babel({ presets: ["es2015"] }))
        .pipe(uglify())
        .pipe(gulp.dest(dirs.dest));
    return stream; // Esta sintaxis sincroniza la renderización
                   // con el reinicio de gulp-nodemon
});

// ============================


// ============================
// ===  Jade transpilation  ===

gulp.task("jade", () => {
    const stream = gulp.src("src/**/*.jade")
        .pipe(jade({
            pretty: true,
        }))
        .pipe(gulp.dest(dirs.dest));
    return stream;
});

// ============================
 

// ============================
// ===  Sass transpilation  ===

gulp.task("sass", function () {
    const stream = gulp.src("src/**/*.scss")
        .pipe( sass().on("error", sass.logError) )
        .pipe(cleanCSS(  
            {compatibility: "ie7", debug: debug, level: 2}, 
            (details) => {  // Debuging de la minificación CSS
                if (verbose) {
                    let originSize = details.stats.originalSize;
                    let minSize = details.stats.minifiedSize;

                    let msg = details.name + " -> size : ";
                    msg += originSize + " - min: " + minSize;

                    console.log(msg);
                    console.log("Efficiency: " + details.stats.efficiency);
                }
            }
        ))
        .pipe(gulp.dest(dirs.dest));
  return stream;
});

// ============================


// ============================
// ======    JSHint    =======

gulp.task("lint", () => {
    const stream = gulp.src("src/**.js")
        .pipe(jshint())
        .pipe(jshint.reporter());
    return stream;
 });

// ============================


// ============================
// ======    Nodemon    =======


gulp.task("watch", tasks, () => {
    nodemon({
    	  script: "build/main.js",
    	  watch: ["src"],
    	  tasks: tasks,
    });
});

// ============================

gulp.task("default", ["watch"]);