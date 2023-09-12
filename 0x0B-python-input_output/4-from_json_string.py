#!/usr/bin/python3
"""
    This is a ``from_json_string`` module that return an object
        => Prototype: def from_json_string(my_str):
"""


def from_json_string(my_str):
    """ This is a method that return an object """

    import json

    return (json.loads(my_str))
