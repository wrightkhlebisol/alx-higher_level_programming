#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("{}".format(matrix))
    else:
        for row in matrix:
            if len(row) < 1:
                print()
            else:
                for i in range(len(row)):
                    if i == len(row) - 1:
                        print("{:d}".format(row[i]))
                    else:
                        print("{:d}".format(row[i]), end=' ')
