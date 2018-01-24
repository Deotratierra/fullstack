
const gulp = require("gulp");  // npm install gulp
const jade = require("gulp-jade");  // npm install gulp-jade

gulp.task("jade", function() {
	gulp.src("src/example.jade")
	    .pipe(jade())
	    .pipe(gulp.dest("build/"));
});

gulp.task("default", ["jade"]);
