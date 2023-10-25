#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[2], 'Python is cool', 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
