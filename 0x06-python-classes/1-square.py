#!/usr/bin/python3
""" This is a class Square that defines a square """


class Square:
    """ This is a class Square """

    def __init__(self, size):
        """ Here we define the __init__ function to paas the self size """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be greater than 0")

        self.__size = size
