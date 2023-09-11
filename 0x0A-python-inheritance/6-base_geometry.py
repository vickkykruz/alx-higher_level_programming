#!/usr/bin/python3
"""
    This is a ``base_geometry`` module that define a public instance method
    def area(self) that raise an Expection with a message
"""


class BaseGeometry:
    """ This is class BaseGeometry that hold the method """

    def area(self):
        """ This is a method that rasie an Exception """
        raise Exception("area() is not implemented")
