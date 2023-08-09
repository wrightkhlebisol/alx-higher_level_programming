#!/usr/bin/python3
asc_range = list(range(97, 123))

for n in asc_range:
    if n == 101 or n == 113:
        continue
    print("{}".format(chr(n)), end="")
