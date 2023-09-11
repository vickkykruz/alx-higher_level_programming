#!/usr/bin/python3
"""
    This is a ``is_kind_of_class`` module that check if the object is an
    instance of,or if the object is an instance of a class that inherited
    from specificed class

    def is_kind_of_class(obj, a_class):
"""


def is_kind_of_class(obj, a_class):
    """ This is a method that return True otherwise False """

    if isinstance(obj, a_class):
        return True
    else:
        return False
