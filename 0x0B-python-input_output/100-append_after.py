#!/usr/bin/python3
"""
    This is a ``search_and_update`` module that insert a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """ This is a method that return the appende strings """

    with open(filename, encoding="utf-8") as fd:
        new_list = []

        while True:
            line = fd.readline()
            if line == "":
                break

            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)

    with open(filename, 'w', encoding="utf-8") as fd:
        fd.writelines(new_list)
