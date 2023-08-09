#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

new_num = int(str(number)[-1])

if new_num > 5:
    print(f"Last digit of {number:d} is greater than 5")
if new_num < 6 and new_num != 0:
    print(f"Last digit of {number:d} is less than 6 and not 0")
if new_num == 0:
    print(f"Last digit of {number:d} is 0")
