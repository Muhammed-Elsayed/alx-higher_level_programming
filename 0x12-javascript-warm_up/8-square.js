#!/usr/bin/node
const arg = process.argv[2];
const number = Math.floor(parseInt(arg));

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
