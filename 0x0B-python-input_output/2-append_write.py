#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, 'a') as f:
        return f.write(text)
