#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        return None
    max_int = 0
    for n in my_list:
        if n > max_int:
            max_int = n
    return max_int
