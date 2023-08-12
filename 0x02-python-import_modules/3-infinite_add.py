#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    tot_sum = 0
    if len(sys.argv) > 1:
        for n in range(1, len(sys.argv)):
            tot_sum += int(sys.argv[n])
    print("{}".format(tot_sum))
