#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    # INITIZAILED THE VARIABLE TO PERMORE THE TASKS
    lenght = len(argv)
    # CHECK IF THE ARGUMENT PASSED IS UP TO 4 IN LENGTH
    if lenght != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    num1 = int(argv[1])
    num2 = int(argv[3])
    # CHECK THE OPERATOR IF IS COMPATABLE
    if operator == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif operator == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    elif operator == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    elif operator == '/':
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
