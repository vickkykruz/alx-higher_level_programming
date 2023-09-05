#!/usr/bin/python3
"""
    This is module that prevents the user from dynamically creating new
    instance attributes, except if the new instance attribute is called
    first_name.
"""


class LockedClass:
    """ This is a class that hold the block of code
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """ This is the initaizate method """

        pass
