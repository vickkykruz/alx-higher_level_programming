#!/usr/bin/python3
"""
    This is a ``base_geometry`` module that define the following:

    def area(self): that raise an Exception with a message
    def integer_validator(self, name, value) that validate the value:
        => if value is not an integer raise a TypeError with a message
        => if value is less or equal to 0 raise a ValueError with a message
"""


class BaseGeometry:
    """ This is a class BaseGeometry that hold the functionality """

    def area(self):
        """ This is a method that raises an Exception with a message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This is a method that validate the value """

        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value
