#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        sign, sign_list = sys.argv[2], ["+", "-", "*", "/"]
        if sign not in sign_list:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if sign == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            if sign == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            if sign == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            if sign == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
