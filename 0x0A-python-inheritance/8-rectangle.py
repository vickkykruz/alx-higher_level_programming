#!/usr/bin/python3
"""
    This is a ``rectangle`` module that inherits from ``7-base_geometry.py``

    create a class Rectangle
        def __init__(self, width, height):
            => width and height must be private. No getter and setter
            => width and height must be positive integer validated by
            `integer_validator`
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ This is a method that initaizated the width and height """

        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__height = height
        self.__width = width
