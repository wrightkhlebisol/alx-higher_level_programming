#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        print("0 arguments.")
    else:
        print("{} argument:".format(len(sys.argv) - 1))
        for n in range(1, len(sys.argv)):
            print("{}: {}".format(n, sys.argv[n]))
