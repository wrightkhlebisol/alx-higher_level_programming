#!/usr/bin/python3
"""9-rectangle.py"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Class method for object compare, available in the
        class scope so has access to all class instances"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __str__(self):
        """Print string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return f''
        for i in range(self.__height - 1):
            print("{}".format(str(Rectangle.print_symbol)) * self.__width)
        return f"{str(Rectangle.print_symbol)}" * self.__width

    def __repr__(self):
        """String representation of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
