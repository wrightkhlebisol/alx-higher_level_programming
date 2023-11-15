#!/usr/bin/python3
print(list(range(26, 4)))
for n in list(range(4, 26)):
    print(n)
    print("{}".format(chr(65 + n), end=""))
