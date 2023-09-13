#!/usr/bin/python3
""" 0-add_integer.py """


def add_integer(a, b=98):
    """Add two integers with one named argument"""
    if type(a) not in (int, float):
        raise Exception("a must be an integer")
    if type(b) not in (int, float):
        raise Exception("b must be an integer")
    return int(a) + int(b)
