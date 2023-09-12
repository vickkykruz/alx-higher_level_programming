#!/usr/bin/python3
"""
    This is a ``save_to_json_file`` that writes an Object to a text file,
    using a JSON representation
        => Prototype: def save_to_json(my_ob, filename):
        => You must use the with statement
"""


def save_to_json_file(my_obj, filename):
    """ This is a method that a text file """

    import json

    with open(filename, 'w', encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
