#!/usr/bin/python3
"""
    This is a ``write_file`` that writes a string to a text file (UTF-8) and
    returns the number of charcters written:
        => Prototype: def write_file(filename="", text=""):
        => You must use the with statements
"""


def write_file(filename="", text=""):
    """ This is a method that return the number of chacters wriitten """

    with open(filename, 'w', encoding="utf-8") as fd:
        charLen = fd.write(text)
        return charLen
