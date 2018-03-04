const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass');

// Compile Sass & Inject Into Browser
gulp.task('sass', function(){
  return gulp.src(['node_modules/bootstrap/scss/bootstrap.scss','static/scss/*.scss'])
    .pipe(sass())
    .pipe(gulp.dest("static/css"))
    .pipe(browserSync.stream());
});

// Move JS Files to static/js
gulp.task('js', function(){
  return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js','node_modules/jquery/dist/jquery.min.js','node_modules/popper.js/dist/umd/popper.min.js'])
    .pipe(gulp.dest("static/js"))
    .pipe(browserSync.stream());
});

// Watch Sass & Server
gulp.task('serve', ['sass'], function(){
  browserSync.init({
    server: "./static"
  });

  gulp.watch(['node_modules/bootstrap/scss/bootstrap.scss', 'static/scss/*.scss'], ['sass']);
  gulp.watch("static/*.html").on('change', browserSync.reload);
});

// Move Fonts Folder to static/fonts
gulp.task('fonts', function(){
  return gulp.src('node_modules/font-awesome/fonts/*')
    .pipe(gulp.dest("static/fonts"));
});

// Move Font Awesome CSS to static/css
gulp.task('fa', function(){
  return gulp.src('node_modules/font-awesome/css/font-awesome.min.css')
    .pipe(gulp.dest("static/css"));
});

gulp.task('default', ['js', 'serve', 'fa', 'fonts']);
