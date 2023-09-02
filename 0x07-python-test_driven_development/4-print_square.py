#!/usr/bin/python3
""" Return the printed square with character '#'

    Prototype: def print_square(size)

    size is the size lenght of the square
    size must be an integer, otherwise raise a TypeError with a msg
    "size must be an integer"
    if size is less than 0, raise ValueError with msg "size must be >= 0"
    if size is a float and is less than 0, raise TypeError with "size must be
    an integer"
"""


def print_square(size):
    """ Return the printed square with character '#'
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
