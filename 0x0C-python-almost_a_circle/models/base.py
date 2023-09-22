#!/usr/bin/python3
"""BASE CLASS: models/base.py"""
import json


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
        """Class to json string """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Object from json string """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                new_list = list()
                for list_obj in list_objs:
                    new_list.append(list_obj.to_dictionary())
                file.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all attributes set"""
        dummy_cls = cls(1, 1, 1, 1)
        dummy_cls.update(**dictionary)
        return dummy_cls

    @classmethod
    def load_from_file(cls):
        """Load from file"""
        try:
            file_name = cls.__name__ + ".json"
            with open(file_name, "r") as file:
                json_str = file.read()
                json_list = cls.from_json_string(json_str)
                each_obj = [cls.create(**obj) for obj in json_list]
                return each_obj
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to a CSV file"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                new_str = ""
                for list_obj in list_objs:
                    new_str.append(list_obj.to_dictionary())
                file.write(cls.to_json_string(new_list))

    @classmethod
    def load_from_file_csv(cls):
        """Load from a CSV file"""
        try:
            file_name = cls.__name__ + ".csv"
            with open(file_name, "r") as file:
                json_str = file.read()
                json_list = cls.from_json_string(json_str)
                each_obj = [cls.create(**obj) for obj in json_list]
                return each_obj
        except FileNotFoundError:
            return []
