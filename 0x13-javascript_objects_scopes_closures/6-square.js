#!/usr/bin/node

/* Write a class Square that defines a square and inherits from Square of
 * 5-square.js:
 */

const PrevSquare = require('./5-square');

module.exports = class Square extends PrevSquare {
  charPrint (letter) {
    if (letter === undefined) {
      for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
    } else {
      for (let i = 0; i < this.height; i++) console.log(letter.repeat(this.width));
    }
  }
};
