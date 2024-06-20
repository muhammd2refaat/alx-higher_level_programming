#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    let i;
    let j;
    let row = '';
    if (c === undefined) {
      c = 'X';
    }
    for (i = 0; i < this.width; i++) {
      row += c;
    }
    for (j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
}

module.exports = Square;
