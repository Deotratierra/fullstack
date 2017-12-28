"use strict";

import gulp from "gulp";
import uglify from "gulp-uglify";
import babel from "gulp-babel";

const dirs = {
    src: "src/*.js",
    dest: "build"
}

gulp.task("build", () => {
    return gulp.src(dirs.src)
        .pipe(babel({ presets: ['es2015'] }))
        .pipe(uglify())
        .pipe(gulp.dest(dirs.dest));
});

gulp.task("watch", () => {
    gulp.watch(dirs.src, ["build"]);
})

gulp.task("default", ["watch"]);


/* ==========   .babelrc   =============

{
    "presets": ["es2015"]
}

========================================

==========   package.json   ============

"devDependencies": {
    "babel-core": "^6.26.0",
    "babel-preset-es2015": "^6.24.1",
    "babel-register": "^6.26.0",
    "gulp": "^3.9.1",
    "gulp-babel": "^7.0.0",
    "gulp-uglify": "^3.0.0"
  }

========================================