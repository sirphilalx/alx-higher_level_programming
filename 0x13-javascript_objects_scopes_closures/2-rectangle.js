#!/usr/bin/node

/*
 * initialised Rectangle class with a condition
 */

class Rectangle{
  constructor (w, h) {
    if (w > 0 && h > 0){
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
