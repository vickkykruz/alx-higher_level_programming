#!/usr/bin/python3
"""
    This is a ``rectangle`` module that create a class Rectangle that is
    inherit from BaseGeometry.

    The width and height: def __init__(self, width, height):
        => width and height must be private. No getter or setter
        => width and height must be positive integers validate by
        integer_validator

    The area() method must be implemented
    print() should print, and str() should return the following rectangle with
    a message
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a class Rectangle that inherit the BaseGeometry module """

    def __init__(self, width, height):
        """ This is a method the initizated the width and height """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__height = height
        self.__width = width

    def __str__(self):
        """ This is a method that print the class instance """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ This is a method that calculate the area of a rectangle """
        res = self.__width * self.__height

        return res
