#!/usr/bin/node
const numArgs = process.argv.length - 2;
if (numArgs >= 1) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
