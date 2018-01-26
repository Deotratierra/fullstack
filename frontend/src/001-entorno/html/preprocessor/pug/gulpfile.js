
const gulp = require("gulp");
const jade = require("gulp-jade");

gulp.task("jade", function() {
	gulp.src("src/example.jade")
	    .pipe(jade())
	    .pipe(gulp.dest("build/"));
});

gulp.task("default", ["jade"]);