#!/usr/bin/python3
"""
    This is the "add_integer" module

    This add_integer module add two integer as one function, For example
"""
def add_integer(a, b=98):
    """ Return the added integer of a and b.
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
