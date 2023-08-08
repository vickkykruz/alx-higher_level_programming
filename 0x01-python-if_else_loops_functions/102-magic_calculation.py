#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return 0
    elif c > b:
        return a + b
    else:
        return a * b - c
