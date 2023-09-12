#!/usr/bin/python3
"""
    This is a ``student_to_json_filter`` that defines a student by:
        => Public instance attributes:
            => first_name
            => last_name
            => age
        => Instantion with first_name, last_name and age:
            def __init__(self, first_name, last_name, age):
        => Public def to_json(self, attrs=None):
"""


class Student:
    """ This is a class Student that define a student """

    def __init__(self, first_name, last_name, age):
        """ This is a method that initizated the object """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This is a method that retrieves a dictionary reprsentation """

        if type(attrs) is list:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__

            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}

            return self.__dict__
