#!/usr/bin/python3
"""
    This is a ``student_to_disk_and_reload`` that define a student
        => Public instance attributes:
            => first_name
            => last_name
            => age
        => Instantiation with first_name, last_name and age:
            def __init__(self, first_name, last_name, age):
        => Public method def to_json(self, attrs=None): that retrieves a
        dictionary reprsentation of a Studnet
        => Public method def reload_from_json(self, json):
"""


class Student:
    """ This is a class Student that defines student """

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

    def reload_from_json(self, json):
        """ This is a method that replaces all the attributes """

        for key, value in json.items():
            setattr(self, key, value)
