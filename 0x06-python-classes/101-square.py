#!/usr/bin/python3
''' This is a module that define a square '''


class Square:
    """ This a class that contains private instance size attribute """

    def __init__(self, size=0, position=(0, 0)):
        """ This is a method that Initalizated self """

        self.size = size
        self.position = position

    def __str__(self):
        """ This is a method that pass the value """

        ch = ""
        if self.size == 0:
            return ch
        for i in range(self.position[1]):
            ch += "\n"

        for i in range(self.size):
            for k in range(self.position[0]):
                ch += " "
            for j in range(self.size):
                ch += "#"
            if i != self.size - 1:
                ch += "\n"
        return ch

    @property
    def size(self):
        """ This is a method that return the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ This is a method that set the size of the value """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """ This is a method that return the position of teh square """
        return self.__position

    @position.setter
    def position(self, value):
        """ This is a method that set the position of the square value """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ This is a method that return the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ This is a method that return the character # """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
