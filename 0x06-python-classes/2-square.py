#!/usr/bin/python3
# square class

class Square:
    """ square class """

    def __init__(self, size=0):
        """init
        Args
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area
        Returns
            the current square area
        """

        return (self.__size * self.__size)
