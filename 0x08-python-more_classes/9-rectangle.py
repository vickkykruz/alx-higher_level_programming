#!/usr/bin/python3
"""
    This module is that contains a Rectangle class with
    width and height instance attribute and also
    a property and property setter.
"""


class Rectangle:
    """
        This is a rectangle class with width and height properties
        and a perimeter and area methods and a class method
    """

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ This is compare two rectangles """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
            This is a method returns a new Rectangle instance with width
            = height = size
        """

        return Rectangle(size, size)

    def __init__(self, width=0, height=0):
        """ This methid initialize a new instance """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ This is a method that return the string representation """

        s = ""
        if self.perimeter() == 0:
            return s

        for i in range(self.__height):
            for j in range(self.__width):
                s += str(self.print_symbol)
            if i < self.__height - 1:
                s += "\n"

        return s

    def __repr__(self):
        """
            This is a method that return the string representation
            to be able to recreate a new instance
        """

        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

        return s

    def __del__(self):
        """ This method calls when an instance is being deleted """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ This methid get the width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ This methid set the width property """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ This methid get the height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ This methid set the height property """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ This methid returns the area of the rectangle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ This methid returns the perimeter of the rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
