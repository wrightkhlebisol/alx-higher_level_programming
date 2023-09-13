#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """Save object to json"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
