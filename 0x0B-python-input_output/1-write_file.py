#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """write text to a file"""
    with open(filename, 'w') as f:
        return f.write(text)
