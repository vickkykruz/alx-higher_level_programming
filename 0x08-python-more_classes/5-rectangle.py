#!/usr/bin/python3
""" This is a 5-rectangle module """


class Rectangle:
    """ This is a class Rectangle that store the block of code """

    def __init__(self, width=0, height=0):
        """ This is an initizated method """

        self.width = width
        self.height = height

    def __str__(self):
        """ This is a methid that print the rectangke with character "#"
        """

        s = ""
        if self.perimeter() == 0:
            return s

        for i in range(self.__height):
            for j in range(self.__width):
                s += "#"
            if i < self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        """
            This is a method that return the string representation
        """

        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return s

    def __del__(self):
        """ This methid is called when the instance is deleted """
        print("Bye rectangle...")

    @property
    def width(self):
        """ This is a metgod that reteive the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is a method that set the value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ This is a method that reteive the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is a method that set the value """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ This is a method that calculate the area of a rectangle """
        res = self.__height * self.__width
        return res

    def perimeter(self):
        """ This is a method that calculate the perimeter of a rectangel """
        if self.__width == 0 or self.__height == 0:
            return 0

        res = 2 * (self.__width + self.__height)
        return res
