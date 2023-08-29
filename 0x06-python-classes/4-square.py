#!/usr/bin/python3
""" This is a python file that define the square """


class Square:
    """ This is a class Square the contain the block of code """

    def __init__(self, size=0):
        """ This is the initiatiated method """
        self.__size = size

    @property
    def size(self):
        """ This is the method that retrive the value """
        return self.__size

    @size.setter
    def size(self, value):
        """ This is the method that set the value """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ this is a method that calculate the area of the square """
        result = self.__size ** 2
        return result
