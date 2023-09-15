#!/usr/bin/python3
"""
    This is a ``square`` module that does the following:
        => Creatte a class Square inherit from Rectangle
        => Class constructor: def __init__(self, size, x=0, y=0, id=None)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is a class Square that inherit from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ This is a method that initalizaed the instances """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ This is a method that retrieve that value """
        return self.width

    @size.setter
    def size(self, value):
        """ This is a method that set the value to the instance """
        
        self.width = value
        self.height = value

    def __str__(self):
        """ This is a method that return the string """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)
