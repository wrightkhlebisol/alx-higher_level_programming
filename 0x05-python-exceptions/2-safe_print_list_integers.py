#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                num_printed += 1
        print()
        return num_printed
    except (TypeError, ValueError):
        print()
        return num_printed
