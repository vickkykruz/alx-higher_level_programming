#!/usr/bin/node

/* Write a class Rectangle that defines a rectangle: */

module.exports = class Rectangle {
  constructor (w, h) {
    // Checking the width and the height
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
