#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """Read given file"""
    with open(filename) as t_file:
        print(t_file.read(), end='')
