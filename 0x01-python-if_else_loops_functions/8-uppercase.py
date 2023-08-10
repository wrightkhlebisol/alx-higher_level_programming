#!/usr/bin/python3
def uppercase(str):
    new_chr = ""
    for ch in str:
        ch_n = ord(ch)
        if (ch_n >= 97 and ch_n <= 122):
            new_chr += chr(ch_n - 32)
        else:
            new_chr += ch

    print(new_chr)
