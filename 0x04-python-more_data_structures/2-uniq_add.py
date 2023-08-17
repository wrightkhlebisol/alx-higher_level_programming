#!/usr/bin/python3
def uniq_add(my_list=[]):
    _sum = 0
    if len(my_list) > 0:
        for val in set(my_list):
            _sum += val
    return _sum
