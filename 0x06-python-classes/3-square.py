#!/usr/bin/python3
""" This source is calculate the area of the square """


class Square:
    """ This is a class that contain the block of code """

    def __init__(self, size=0):
        """ This is the initization method of the size """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ This is a method that calcluate the are of the square """

        result = self.__size ** 2
        return result
