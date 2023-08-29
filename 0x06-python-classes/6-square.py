#!/usr/bin/python3
""" This is a python file that defines a square """


class Square:
    """ This is a class that contains the blockof codes """

    def __init__(self, size=0, position=(0, 0)):
        """ This is a method that initizated the vlaue """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ This is a method that retrieve the value """
        return self.__size

    @size.setter
    def size(self, value):
        """ This is a method that set the value """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """ This is a method that return the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """ This is a method that set the position of the square value """

        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ This is method that return the calculated area of a square """
        result = self.__size ** 2
        return result

    def my_print(self):
        """ This is a method that return the printed square characters """
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
