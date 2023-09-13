#!/usr/bin/python3
"""7-add_item.py"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def load_add_save(*args):
    """Load a file, append to it and then save it"""
    filename = "add_item.json"
    cmd_args = sys.argv[1:]

    file_content = load_from_json_file(filename)
    if file_content is None:
        save_to_json_file(cmd_args, filename)
    else:
        file_content.extend(cmd_args)
        save_to_json_file(file_content, filename)


load_add_save()
