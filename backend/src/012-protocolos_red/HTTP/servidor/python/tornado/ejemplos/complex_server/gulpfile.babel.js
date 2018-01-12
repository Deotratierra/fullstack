"use strict";

import gulp from "gulp";
const gulpsync = require("gulp-sync")(gulp);
import babel from "gulp-babel";
import jshint from "gulp-jshint";
import uglify from "gulp-uglify";
import cleanCSS from "gulp-clean-css";
import jade from "gulp-jade";
import sass from "gulp-sass";
import webpack from "webpack-stream";
import named from "vinyl-named";
import shell from "gulp-shell";
import walk from "walk";
import path from "path";
import fs from "fs";

const debug = true,
      verbose = true;

const dirs = {
    src: "src",
    dest: "build"
};

let build_tasks = ["es6", "webpack", "jade", "sass", "python-copy"];
const lint_tasks = ["pylint", "jshint"];


// ============================
// ====  ES6 compilation  =====

gulp.task("es6", () => {
    const stream = gulp.src(dirs.src + "/**/*.js")
        .pipe(babel({
            presets: ["es2015"]
        }))
        .pipe(uglify())
        .pipe(gulp.dest(dirs.dest));
    return stream;
});

// ============================


// ============================
// ===  Jade transpilation  ===

gulp.task("jade", () => {
    const stream = gulp.src(dirs.src + "/**/*.jade")
        .pipe(jade({
            pretty: true,
            compileDebug: true
        }))
        .pipe(gulp.dest(dirs.dest));
    return stream;
});

// ============================


// ============================
// ===  Sass transpilation  ===

gulp.task("sass", () => {
    const stream = gulp.src(dirs.src + "/**/*.scss")
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
// ====     Webpack     ====

// Modularized bundles:
// For every scene, and for every page
// in the scene there's a bundled js file

const browser_files = []
const src_scenes_dir = path.join("src", "scenes");
const scenes = fs.readdirSync(src_scenes_dir);

const options = {
    listeners: {
        file: (root, fileStats, next) => {
            // Get scenes index.js
            let base_root_dir = path.basename(root);
            if (scenes.indexOf(base_root_dir) > -1 || // global scene js
                base_root_dir[0] == base_root_dir[0].toUpperCase()) { // concrete scene js
                if (path.extname(fileStats.name) == ".js") {
                    browser_files.push( path.join(root, fileStats.name) );
                }
            }
            next();
        }
    }
};

const walker = walk.walkSync(src_scenes_dir, options);

gulp.task("webpack", () => {
    return gulp.src(browser_files)
        .pipe(named())
        .pipe(webpack())
        .pipe(gulp.dest(dirs.dest))
})


// ============================


// ============================
// ====    Python build    ====  (copy - paste)


gulp.task("python-copy", () => {
    return gulp.src(dirs.src + "/**/**.py")
        .pipe( gulp.dest(dirs.dest) )
});


// ============================


// ============================
// =======    JSHint    =======

gulp.task("jshint", () => {
    const stream = gulp.src(dirs.src + "/*/**.js")
        .pipe(jshint())
        .pipe(jshint.reporter());
    return stream;
 });

// ============================


// ============================
// =======    pylint    =======

// Task

gulp.task("pylint", shell.task([
    "cd src && " + process.env.VIRTUAL_ENV + "/bin/pylint src",
]));

// ============================
// ========    TASKS    =======

// RUNSERVER
gulp.task("runserver", shell.task([
    "cd build && python3 main.py",
]));

// LINT
gulp.task("lint", lint_tasks);

// BUILD
gulp.task("build", build_tasks);

// ============================

gulp.task("default", gulpsync.sync( build_tasks.concat(["runserver"])) );
