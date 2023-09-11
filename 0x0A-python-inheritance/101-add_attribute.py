#!/usr/bin/python3
"""
    This is a ``add_attribute`` that add a new attribute to an object if it's
    possible
"""


def add_attribute(obj, name, value):
    """ This is a function that add an attriubute """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
