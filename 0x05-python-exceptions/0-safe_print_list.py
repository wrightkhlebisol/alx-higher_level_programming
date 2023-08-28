#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
        return i
    except (ValueError, IndexError):
        print("Invalid x")
    return x
