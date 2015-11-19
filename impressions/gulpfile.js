/*global -$ */
'use strict';
// generated on 2015-03-30 using generator-gulp-webapp 0.3.0
var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var browserSync = require('browser-sync');
var reload = browserSync.reload;

gulp.task('styles', function() {
  return gulp.src('app/styles/main.scss')
    .pipe($.sourcemaps.init())
    .pipe($.sass({
      outputStyle: 'nested', // libsass doesn't support expanded yet
      precision: 10,
      includePaths: ['.'],
      onError: console.error.bind(console, 'Sass error:')
    }))
    .pipe($.postcss([
      require('autoprefixer-core')({
        browsers: ['last 1 version']
      })
    ]))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('.tmp/styles'))
    .pipe(reload({
      stream: true
    }));
});

gulp.task('styles:adomattic', function() {
  return gulp.src('app/styles/main.scss')
    .pipe($.sourcemaps.init())
    .pipe($.sass({
      outputStyle: 'nested', // libsass doesn't support expanded yet
      precision: 10,
      includePaths: ['.'],
      onError: console.error.bind(console, 'Sass error:')
    }))
    .pipe($.postcss([
      require('autoprefixer-core')({
        browsers: ['last 1 version']
      })
    ]))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('../../apps/dashboard/static/impressions/dist/'))
    .pipe(reload({
      stream: true
    }));
});


gulp.task('adomattic', function() {
  var uglifyOptions = {
    mangle: {
      toplevel: true,
    },
    compress: {
      sequences: true,
      dead_code: true,
      conditionals: true,
      booleans: true,
      unused: true,
      if_return: true,
      join_vars: true,
      //drop_console: true
    },
    outSourceMap: true
  };

  var sizeOptions = {
    showFiles: true
  };

  gulp.src(['bower_components/axios/dist/axios.js', 'app/scripts/ai.js'])
    .pipe($.sourcemaps.init())
      .pipe($.concat('aware.js'))
      .pipe($.uglify(uglifyOptions))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('.tmp/scripts'))
    .pipe($.size(sizeOptions));
});

gulp.task('adomattic:live', ['styles:adomattic'], function() {
  var uglifyOptions = {
    mangle: {
      toplevel: true,
    },
    compress: {
      sequences: true,
      dead_code: true,
      conditionals: true,
      booleans: true,
      unused: true,
      if_return: true,
      join_vars: true,
      drop_console: true
    },
    //outSourceMap: true
  };

  var sizeOptions = {
    showFiles: true
  };

  gulp.src(['bower_components/axios/dist/axios.js', 'app/scripts/ai.js'])
    .pipe($.concat('aware.js'))
    .pipe($.replace("base: 'http://localhost:9050/api/'", "base: 'https://app.intentaware.com/api/'"))
    .pipe($.replace("https://github.com/mzabriskie/axios/blob/master/README.md#response-api", "There was an error!"))
    .pipe($.uglify(uglifyOptions))
    .pipe(gulp.dest('../../apps/dashboard/static/impressions/dist/'))
    .pipe($.size(sizeOptions));
});

gulp.task('adomattic:stage', ['styles:adomattic'], function() {
  var uglifyOptions = {
    mangle: {
      toplevel: true,
    },
    compress: {
      sequences: true,
      dead_code: true,
      conditionals: true,
      booleans: true,
      unused: true,
      if_return: true,
      join_vars: true,
      drop_console: true
    },
    //outSourceMap: true
  };

  var sizeOptions = {
    showFiles: true
  };

  gulp.src(['bower_components/axios/dist/axios.js', 'app/scripts/ai.js'])
    .pipe($.concat('aware.js'))
    .pipe($.replace("base: 'http://localhost:9050/api/'", "base: 'http://stage.intentaware.com/api/'"))
    .pipe($.replace("https://github.com/mzabriskie/axios/blob/master/README.md#response-api", "There was an error!"))
    .pipe($.uglify(uglifyOptions))
    .pipe(gulp.dest('../../apps/dashboard/static/impressions/dist/'))
    .pipe($.size(sizeOptions));
});


gulp.task('jshint', function() {
  return gulp.src('app/scripts/**/*.js')
    .pipe(reload({
      stream: true,
      once: true
    }))
    .pipe($.jshint())
    .pipe($.jshint.reporter('jshint-stylish'))
    .pipe($.if(!browserSync.active, $.jshint.reporter('fail')));
});

gulp.task('html', ['styles'], function() {
  var assets = $.useref.assets({
    searchPath: ['.tmp', 'app', '.']
  });

  return gulp.src('app/*.html')
    .pipe(assets)
    .pipe($.if('*.js', $.uglify()))
    .pipe($.if('*.css', $.csso()))
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.if('*.html', $.minifyHtml({
      conditionals: true,
      loose: true
    })))
    .pipe(gulp.dest('dist'));
});

gulp.task('images', function() {
  return gulp.src('app/images/**/*')
    .pipe($.cache($.imagemin({
      progressive: true,
      interlaced: true,
      // don't remove IDs from SVGs, they are often used
      // as hooks for embedding and styling
      svgoPlugins: [{
        cleanupIDs: false
      }]
    })))
    .pipe(gulp.dest('dist/images'));
});

gulp.task('fonts', function() {
  return gulp.src(require('main-bower-files')({
      filter: '**/*.{eot,svg,ttf,woff,woff2}'
    }).concat('app/fonts/**/*'))
    .pipe(gulp.dest('.tmp/fonts'))
    .pipe(gulp.dest('dist/fonts'));
});

gulp.task('extras', function() {
  return gulp.src([
    'app/*.*',
    '!app/*.html'
  ], {
    dot: true
  }).pipe(gulp.dest('dist'));
});

gulp.task('clean', require('del').bind(null, ['.tmp', 'dist']));

gulp.task('serve', ['styles', 'fonts', 'adomattic'], function() {
  browserSync({
    notify: false,
    port: 9000,
    server: {
      baseDir: ['.tmp', 'app'],
      routes: {
        '/bower_components': 'bower_components'
      }
    }
  });

  // watch for changes
  gulp.watch([
    'app/*.html',
    'app/scripts/**/*.js',
    'app/images/**/*',
    '.tmp/fonts/**/*'
  ]).on('change', reload);

  gulp.watch('app/styles/**/*.scss', ['styles']);
  gulp.watch('app/scripts/ai.js', ['adomattic']);
  gulp.watch('app/fonts/**/*', ['fonts']);
  gulp.watch('bower.json', ['wiredep', 'fonts']);
});

// inject bower components
gulp.task('wiredep', function() {
  var wiredep = require('wiredep').stream;

  gulp.src('app/styles/*.scss')
    .pipe(wiredep({
      ignorePath: /^(\.\.\/)+/
    }))
    .pipe(gulp.dest('app/styles'));

  gulp.src('app/*.html')
    .pipe(wiredep({
      exclude: ['bootstrap-sass-official', 'axios'],
      ignorePath: /^(\.\.\/)*\.\./
    }))
    .pipe(gulp.dest('app'));
});

gulp.task('build', ['jshint', 'html', 'images', 'fonts', 'extras'], function() {
  return gulp.src('dist/**/*').pipe($.size({
    title: 'build',
    gzip: true
  }));
});

gulp.task('default', ['clean'], function() {
  gulp.start('build');
});
