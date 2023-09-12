#!/usr/bin/python3
"""
    This is a ``json_string`` that return the JSON reprsentation of an object
    (string)
        => Prototype: def to_json_string(my_obj):
"""


def to_json_string(my_obj):
    """ This is a method that return the JSON reprsentation of an object """

    import json

    return (json.dumps(my_obj))
