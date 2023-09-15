#!usr/bin/python3
"""
    This is a ``base_class`` module, we are tasked to do the following:
        => Create a class Base
            => Create a private class attribute __nb_objects = 0
            => Create a class construct: def __init__(self, id=None):
"""


class Base:
    """ This is a class Base that implemant the following """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is a method the intizated the instance """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
