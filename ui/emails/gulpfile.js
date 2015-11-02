'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

gulp.task('compile', function() {
    gulp.src('./src/*.html')
      .pipe($.inlineCss({}))
      .pipe(gulp.dest('build/'));
  });

gulp.task('default', ['compile'], function() {

  });