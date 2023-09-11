#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """"Inherits from list"""

    def print_sorted(self):
        """Prints sorted list"""
        new_list = list(self)
        list.sort(self)
        print(new_list)
