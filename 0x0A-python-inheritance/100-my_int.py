#!/usr/bin/python3
"""
    This is a ``my_int`` module that inherit from int.
"""


class MyInt(int):
    """ This is a class MyInt that inherits from int """

    def __eq__(self, obj):
        """ This is a method that call for equal to comparsion """
        return super().__ne__(obj)

    def __ne__(self, obj):
        """ This is a method that nt equal to comparsion """
        return super().__eq__(obj)
