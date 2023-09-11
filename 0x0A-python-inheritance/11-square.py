#!/usr/bin/python3
"""
    This is a ``square`` module that create a class Square that inherits from
    Rectangle.

    Define with size: def __init__(self, size):
        => size must be private. No getter or setter
        => size must be a positive integer, validated by intefer_validator

    The area() method must be implemented
    print() should print, and str() should return, with a message
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is a class Square that inherit from Rectangle """

    def __init__(self, size):
        """ This is a initizated method """

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ This is a method that return the string """
        return ("[Square] {}/{}".format(self.__size, self.__size))
