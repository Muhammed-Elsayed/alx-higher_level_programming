#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    console.log(this.size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
