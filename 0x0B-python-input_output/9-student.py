#!/usr/bin/python3
"""
    This is a ``student_to_json`` that defines a student by:
        => Public instance attribute:
            => first_name
            => last_name
            => age
        => instantiation with first_name, last_name & age:
            def __init__(self, first_nam, last_name, age):
        => Public method def to_json(self):
"""


class Student:
    """ This is a class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """ This is a method that initizated the following object """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This is a method that retrieve a dictionary reprsentation """

        return (self.__dict__)
