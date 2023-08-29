#!/usr/bin/python3
""" This is a class Square that defines a square by """


class Square:
    """ This a class Square weere the block of code is presented """

    def __init__(self, size=0):
        """ This is a method that define the init function of the size """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = 0
