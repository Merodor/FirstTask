var gulp = require('gulp');
var exec = require('child_process').exec;

var options = {
  continueOnError: false, // default = false, true means don't emit error event
  pipeStdout: false, // default = false, true means stdout is written to file.contents
  customTemplatingThing: "test" // content passed to lodash.template()
};

var reportOptions = {
	err: true, // default = true, false means don't write err
	stderr: true, // default = true, false means don't write stderr
	stdout: true // default = true, false means don't write stdout
};

gulp.task('default', (cb) => {
  var watcher = gulp.watch('./**/*.py', { events: 'all' });

  watcher.on('all', function(status, filename) {
    console.log(`\nRunning >>\n \nTutorial ${filename.replace("\\", "\nfile ")} was changed runing python \n-------------------------------------------------------------------`);

    exec(`python "${ __dirname}/${filename}"`, function (err, stdout, stderr) {
      console.log(stdout);
      console.log(stderr);
      console.log("-------------------------------------------------------------------");
      cb(err);
    });
  });
})
