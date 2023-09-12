#!/usr/bin/python3
"""
    This is a ``class_to_json`` module that return the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serializated of an object:
        => Prototype: def class_to_json(obj):
"""


def class_to_json(obj):
    """ This is method that return the simple data sructure """

    return (obj.__dict__)
