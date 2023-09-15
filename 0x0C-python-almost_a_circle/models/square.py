#!/usr/bin/python3
"""
    This is a ``square`` module that does the following:
        => Creatte a class Square inherit from Rectangle
        => Class constructor: def __init__(self, size, x=0, y=0, id=None)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is a class Square that inherit from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ This is a method that initalizaed the instances """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ This is a method that retrieve that value """
        return self.width

    @size.setter
    def size(self, value):
        """ This is a method that set the value to the instance """
        
        self.width = value
        self.height = value

    def __str__(self):
        """ This is a method that return the string """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)

    def update(self, *args, **kwargs):
        """ This is a method that assings sttribute """

        i = 0
        attr = ["id", "size", "x", "y"]

        if not args:
            for key, val in kwargs.items():
                if key in attr:
                    setattr(self, key, val)
        else:
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
                if i > 3:
                    break

    def to_dictionary(self):
        """ This is a method that return the dictionary reprsentation of a
            Square
        """

        attrs = ["id", "size", "x", "y"]
        dic_t = {}

        for attr in attrs:
            val = getattr(self, attr)

            dic_t[attr] = val

        return dic_t
