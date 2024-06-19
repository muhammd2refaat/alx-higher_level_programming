#!/usr/bin/node
// isNaN() is used to check if the argument is a number
if (isNaN(process.argv[2] || process.argv[2] === undefined)) {
  console.log('Not a number');
} else { // parseInt() is used to convert the argument to an integer
  console.log('My number: ' + parseInt(process.argv[2]));
}
