#!/usr/bin/python3
"""
    This is a ``first_rectangle`` module that does the following:
        => Create a Rectangle class
        => Create a private instance attribute, each with its own public
            getter and setter
                A. __width -> width
                B. __height -> height
                C. __x -> x
                D. __y -> y
        => Class construct: def __init__(self, width, height, x=0, y=0,
                            id=None)
"""


from models.base import Base


class Rectangle(Base):
    """ This is a class Rectangle that inherit the class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is a method that intializated the following instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ This is a method that reteiver value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is a method that set the value to the instance """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ This is a method that retrives value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is a method that set the value of the instance """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ This is a method that retrieve that value of the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ This is a method that set the value of the instance """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ This is a method that retrives the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ This is a method that set the value of the instance """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """ This is a method the return the string """
        return "[Rectangle ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                self.__width, self.__height)

    def area(self):
        """ This is a method that return the area of a rectangle """
        return (self.__height * self.__width)

    def display(self):
        """ This is a public method that prints in stdout the Rectangle
            instance with the charcter "#"
        """

        for y in range(self.__y):
            print()

        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """ This is a method that assigns an argument to each attribute """

        i = 0
        attr = ["id", "width", "height", "x", "y"]
        for arg in args:
            setattr(self, attr[i], arg)
            i += 1
            if i > 4:
                break
