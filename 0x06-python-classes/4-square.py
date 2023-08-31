#!/usr/bin/python3
"""4-square.py"""


class Square:
    """Access and update private attribute"""

    def __init__(self, size=0):
        """Initialize the class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return square of size as area"""
        return self.size ** 2
