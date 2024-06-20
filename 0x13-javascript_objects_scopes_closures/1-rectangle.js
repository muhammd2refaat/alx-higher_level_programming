#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // constructor receives two arguments w and h, and initializes the instance attributes width and height
    // this refers to the current object
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
