#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let i = 0;
      let j = 0;
      let rect = '';
      while (i < this.height) {
        while (j < this.width) {
          rect += 'X';
          j++;
        }
        console.log(rect);
        i++;
      }
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
