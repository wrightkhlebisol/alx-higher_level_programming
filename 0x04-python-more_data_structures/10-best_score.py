#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    max_val = 0
    if a_dictionary is None:
        return None
    for key in list(a_dictionary):
        if a_dictionary[key] > max_val:
            max_val = a_dictionary[key]
            max_key = key
    return max_key
