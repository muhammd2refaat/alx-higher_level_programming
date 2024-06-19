#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('X'.repeat(args[0]));
  }// repeat() is used to repeat a string
}
