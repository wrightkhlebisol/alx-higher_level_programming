#!/usr/bin/python3
def fizzbuzz():
    nums = list(range(1, 101))
    for n in nums:
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")
