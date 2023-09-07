#!/usr/bin/python3
"""4-rectangle.py"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialization method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Print string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return f''
        for i in range(self.__height - 1):
            print("#" * self.__width)
        return f"#" * self.__width

    def __repr__(self):
        """String representation of rectangle"""
       # return repr(self)
        pass
