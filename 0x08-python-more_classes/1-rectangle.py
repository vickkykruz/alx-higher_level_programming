#!/usr/bin/python3
"""
    This is a rectangle module that define the class Rectangle
"""


class Rectangle:
    """ This is a class Rectangle that does the block of code """
    def __init__(self, width=0, height=0):
        """ This is the initalize method """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Return the retrive width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the self width to the given value """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Return the retrive height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the self height to the given value """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
