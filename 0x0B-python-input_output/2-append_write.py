#!/usr/bin/python3
"""
    This is a ``append_write`` module that append a string at the end of a
    text file (UTF*) and returns the number of charcters added:
        => Prototype: def append_write(filename="", text=""):
        => You must use the with statement
        => if the file doesn't exist, it should be created
"""


def append_write(filename="", text=""):
    """ This is a method that return the number of characters """
    with open(filename, 'a', encoding="utf-8") as fd:
        charLen = fd.write(text)
        return charLen
