#!/usr/bin/python3
""" This function prints a text with 2 new lines after each of these
characters "., ?, and :"

    Prototype: def text_indentation(text)
    text must be a string, otherwise raise TypeError with msg "text must be a
    string"
    There should be no space at the beinning or at the end of each printed
    line
"""


def text_indentation(text):
    """ Return the printed text with 2 new lines after these characters
    "., ?, :"
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print()
            print()
            while (i + 1 != len(text) and text[i + 1] == " "):
                i += 1
        i += 1
