#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
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
    } else {
      this.print();
    }
  }
}

module.exports = Square;
