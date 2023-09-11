#!/usr/bin/python3
"""100-my_int.py"""


class MyInt(int):
    """Inherits from int"""

    def __eq__(self, value):
        """Implements equal to"""
        if self - value == 0:
            return False
        else:
            return True

    def __ne__(self, value):
        """Implements not equal to"""
        if self - value == 0:
            return True
        else:
            return False
