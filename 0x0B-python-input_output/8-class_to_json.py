#!/usr/bin/python3
"""8-class_to_json.py"""
import json


def class_to_json(obj):
    """dictionary description with simple data structure"""
    return json.dumps(obj.__dict__)
