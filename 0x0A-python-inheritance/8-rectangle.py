#!/usr/bin/python3
"""8-rectangle.py"""


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
