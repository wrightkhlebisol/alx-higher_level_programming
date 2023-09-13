#!/usr/bin/python3
""" 0-add_integer.py """


def add_integer(a, b=98):
    """Add two integers with one named argument"""
    try:
        return int(a) + int(b)
    except SyntaxError as e:
        print(e, "Syntax error")
