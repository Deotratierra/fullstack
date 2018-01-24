"use strict"

var gulp = require("gulp");                   // npm i gulp
var browserify = require("browserify");       // npm i browserify
var through = require("through2");            // npm i trough2
var buffer = require("vinyl-buffer");         // npm i vinyl-buffer
var gutil = require("gulp-util");             // npm i gulp-util
var tap = require("gulp-tap");                // npm i gulp-tap

var dirs = {
    src: "./src/",
    dist: "./dist/"
}

var browser_source_files = {
    a: {path: "moduloA/index.js", dir: "moduloA"},
    b: {path: "moduloB/index.js", dir: "moduloB"}
}


gulp.task("browserificar", function() {
    for (var index in browser_source_files) {

        gulp.src(dirs.src + browser_source_files[index].path, {read: false})

        .pipe(tap(function(file){
            gutil.log("Bundling " + file.path);

            file.contents = browserify(file.path, {debug: true}).bundle();
        }))

        .pipe(gulp.dest(dirs.dist + browser_source_files[index].dir));
    };
});

gulp.task("default", ["browserificar"]);
