#!/usr/bin/python3
""" This is a python file that defines a square """


class Square:
    """ This is a class Square that conatin the code of the program """

    def __init__(self, size=0):
        """ This is a method that initizated the value """
        self.__size = size

    @property
    def size(self):
        """ This is a method that retiver the value """
        return self.__size

    @size.setter
    def size(self, value):
        """ This is a method that set the value """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ This is a method the calculate the area of the square """
        result = self.__size ** 2
        return result

    def my_print(self):
        """ This is a method that print the area of the shape """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
