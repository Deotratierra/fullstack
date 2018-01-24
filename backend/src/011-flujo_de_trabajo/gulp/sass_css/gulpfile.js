'use strict';
 
var gulp = require('gulp');       // npm i --save-dev gulp
var sass = require('gulp-sass');  // npm i --save-dev gulp-sass
 
gulp.task('sass', function () {
  return gulp.src('*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('.'));
});

gulp.task('watch', function() {
  gulp.watch('*.scss', ['sass']);
});

gulp.task("default", ["watch"]);