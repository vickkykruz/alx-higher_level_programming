#!/usr/bin/python3
"""
    This is a ``load_from_json_file`` module that create an Object from a
    "JSON file"
        => Prototype: def load_from_json_file(filename):
        => You must use the with statement
"""


def load_from_json_file(filename):
    """ This is a method that return the JSON file """

    import json

    with open(filename, 'r', encoding="utf-8") as fd:
        return (json.load(fd))
