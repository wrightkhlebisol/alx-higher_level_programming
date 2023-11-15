#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      return this.print();
    }

    if (this.width && this.height) {
      let i = 0;
      let j = 0;
      let rect = '';
      while (i < this.height) {
        while (j < this.width) {
          rect += c;
          j++;
        }
        console.log(rect);
        i++;
      }
    }
  }
}

module.exports = Square;
