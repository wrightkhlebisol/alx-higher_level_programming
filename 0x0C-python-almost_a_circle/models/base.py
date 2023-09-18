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

    @classmethod 
    def save_to_file(cls, list_objs):
        """Save json to file"""
        file_name = list_objs[0].__class__.__name__ + ".json"
        with open(file_name, 'w') as file:
            if list_objs is None:
                file.write("")
            else:
                new_list = list()
                for list_obj in list_objs:
                    new_list.append(list_obj.to_dictionary())
                file.write(cls.to_json_string(new_list))
