#!/usr/bin/node

/* Write a class Rectangle that defines a rectangle: */

module.exports = class Rectangle {
  // Checking the value of width and height
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
};
