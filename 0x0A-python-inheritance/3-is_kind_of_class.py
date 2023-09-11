#!/usr/bin/python3
"""3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """Is a subclass"""
    return issubclass(obj.__class__, a_class)
