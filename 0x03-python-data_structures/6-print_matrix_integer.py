#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("{}".format(matrix))
    elif len(matrix) <= 1:
        print("{}".format(""))
    else:
        for row in matrix:
            print("{} {} {}".format(row[0], row[1], row[2]))
