#!/usr/bin/python3
"""11-square.py"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Unimplemented area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherit BaseGeometry"""

    def __init__(self, width, height):
        """Initialization method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Implement area"""
        return self.__width * self.__height

    def __str__(self):
        """Print formatted string"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        """Init method"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Implement area"""
        return self.__size ** 2

    def __str__(self):
        """Print formatted string"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
