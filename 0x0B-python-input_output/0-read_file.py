#!/usr/bin/python3
"""
    This is a ``read_file`` that reads a text file (UTF8) and print it to
    stdout:

        => Prototype: def read_file(filename=""):
        => You must use the with statement.
"""


def read_file(filename=""):
    """ This is a function that return printed text """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
