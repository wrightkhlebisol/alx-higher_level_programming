#!/usr/bin/python3
"""2-is_same.py"""


def is_same_class(obj, a_class):
    """Returns Trues if object is an instance of class"""
    return isinstance(obj.__class__, a_class)
