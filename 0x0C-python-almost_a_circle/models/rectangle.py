#!/usr/bin/python3
""" models/rectangle.py """
from models.base import Base


class Rectangle(Base):
    """Class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class initializer"""
        Base.__init__(self, id)

        self.valid_w_h(width, "width")
        self.valid_w_h(height, "height")
        self.valid_x_y(x, "x")
        self.valid_x_y(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def valid_w_h(self, arg, str_arg):
        if type(arg) is not int:
            raise TypeError(f"{str_arg} must be an integer")
        if arg <= 0:
            raise ValueError(f"{str_arg} must be > 0")

    def valid_x_y(self, arg, str_arg):
        
        if type(arg) is not int:
            raise TypeError(f"{str_arg} must be an integer")
        if arg < 0:
            raise ValueError(f"{str_arg} must be >= 0")

    def area(self):
        """Multiply width and height"""
        return self.width * self.height

    def display(self):
        """ Display the rectangle at given position"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args):
        """Update the attributes"""
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.valid_w_h(width, "width")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.valid_w_h(height, "height")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.valid_x_y(x, "x")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.valid_x_y(y, "y")
        self.__y = y

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
