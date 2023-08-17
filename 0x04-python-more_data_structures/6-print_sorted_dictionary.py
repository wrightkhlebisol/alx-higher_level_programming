#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key_list = sorted(a_dictionary)
    for keys in sorted_key_list:
        print("{}: {}".format(keys, a_dictionary[keys]))
