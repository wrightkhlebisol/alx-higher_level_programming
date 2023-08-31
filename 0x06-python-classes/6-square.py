#!/usr/bin/python3
"""5-square.py"""


class Square:
    """Printing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class"""

        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the area position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return square of size as area"""
        return self.size ** 2

    def my_print(self):
        """Print the square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                if (i % self.size) == 0:
                    print()
                print("#" * self.size)
