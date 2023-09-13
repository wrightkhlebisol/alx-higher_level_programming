#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """Load JSON from file"""
    with open(filename) as f:
        return json.load(f)
