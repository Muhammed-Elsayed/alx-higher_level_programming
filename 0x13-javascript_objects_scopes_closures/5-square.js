#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

let Square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

module.exports = Square;
