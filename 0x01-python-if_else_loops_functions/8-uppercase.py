#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ch_n = ord(ch)
        if (ch_n >= 97 and ch_n <= 122):
            print("{}".format(chr(ch_n - 32)), end="")
        else:
            print("{}".format(ch), end="")
