#!/usr/bin/python3
"""
    This is a 2-rectangle module
"""


class Rectangle:
    """ This is a class Rectangle that hold the block of code """
    def __init__(self, width=0, height=0):
        """ This is an initizated module """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ Return the retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is a module that set the value width """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ This is a method reteive the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is a method that set the height value """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This method calculate the area of a rectangle """

        res = self.__width * self.__height
        return res

    def perimeter(self):
        """ Return the perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0

        res = 2 * (self.__height + self.__width)
        return res
