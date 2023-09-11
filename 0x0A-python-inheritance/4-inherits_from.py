#!/usr/bin/python3
"""
    This is a ``inherits_from``module that check object is an instance of a
    class that inherited (directly or indirectly) from the specfied class
"""


def inherits_from(obj, a_class):
    """ This is a method that return True or False """

    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
