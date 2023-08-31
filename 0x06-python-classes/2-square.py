#!/usr/bin/python3
"""2-square.py"""


class Square:
    """Size validating class."""

    def __init__(self, size=0):
        """Initializes the size variable"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
