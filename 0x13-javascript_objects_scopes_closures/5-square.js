#!/usr/bin/node

// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
// You must use the class notation for defining your class and extends
// The constructor of Square takes one argument: size
// The constructor of Rectangle must be called (by using super())
// Add a new method to Square called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X
class Square extends require('./4-rectangle') {
// extends is used to inherit from another class
// require is used to import the Rectangle class
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
