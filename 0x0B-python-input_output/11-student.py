#!/usr/bin/python3
"""10-student.py"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self_dict = self.__dict__
        if attrs is None:
            return self_dict
        else:
            new_dict = {}
            for attr in attrs:
                if self_dict.get(attr) is not None:
                    new_dict[attr] = self_dict.get(attr)
            return new_dict

    def reload_from_json(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
