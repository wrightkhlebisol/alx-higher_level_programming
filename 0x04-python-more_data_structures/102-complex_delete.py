#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary.items():
        if v == value:
            print(a_dictionary[k])
           # del a_dictionary[k]
    return a_dictionary
