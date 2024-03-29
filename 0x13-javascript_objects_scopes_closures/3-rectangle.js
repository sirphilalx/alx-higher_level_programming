#!/usr/bin/node

/*
 * A class Rectangle that defines a rectangle:
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rows = '';
      for (let j = 0; j < this.width; j++) {
        rows += 'X';
      }
      console.log(rows);
    }
  }
}

module.exports = Rectangle;
