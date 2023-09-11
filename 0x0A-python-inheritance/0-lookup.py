#!/usr/bin/python3
"""
 This is a ``lookup`` modules that returns the list of avaliable attributes
    and methods of an object
"""


def lookup(obj):
    """ This function returns the attributes and methods of an object """
    return dir(obj)
