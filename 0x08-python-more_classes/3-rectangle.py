#!/usr/bin/python3
"""
    This is 3-rectangle module that define the rectangle
"""


class Rectangle:
    """ This is a class Rectangle that contains the block of code """

    def __init__(self, width=0, height=0):
        """ This is an initizated method """

        self.width = width
        self.height = height

    def __str__(self):
        """ This is a methid that return the string reprsentation """
        s = ""

        if self.perimeter == 0:
            return 0

        for i in range(self.__height):
            for j in range(self.__width):
                s += "#"
            if i < self.__height - 1:
                s += "\n"
        return s

    @property
    def width(self):
        """ This is a method reteive the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is a method that set the width value """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ This is a method that reteive the height value """
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
        """ This is a method that calculate the area of a rectangle """
        res = self.__height * self.__width
        return res

    def perimeter(self):
        """ This is a methid that calculate the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0

        res = 2 * (self.__width + self.__height)
        return res
