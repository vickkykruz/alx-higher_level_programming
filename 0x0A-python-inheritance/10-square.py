#!/usr/bin/python3
"""
    This is a ``square`` module that inherits from Rectangle

    define size: def __init__(self, size):
        => size must be private. No getter or setter
        => size must be positive integer, validated by integer_validator

    the area() method must be implemented
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is a class Square that inherits from Rectangle """

    def __init__(self, size):
        """ This is a method that initizated the value """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
