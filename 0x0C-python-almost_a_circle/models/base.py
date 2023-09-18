#!/usr/bin/python3
"""BASE CLASS: models/base.py"""


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class init method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        else:
            return str(list_dictionaries)
