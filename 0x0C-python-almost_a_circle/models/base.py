#!usr/bin/python3
"""
    This is a ``base_class`` module, we are tasked to do the following:
        => Create a class Base
            => Create a private class attribute __nb_objects = 0
            => Create a class construct: def __init__(self, id=None):
"""


import json


class Base:
    """ This is a class Base that implemant the following """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is a method the intizated the instance """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """ This is a method that writes the JSON string reprsentation of
            list_objs to a file
        """

        list_dict = []
        file_name = cls.__name__ + '.json'

        if list_objs:
            for obj in list_objs:
                obj_dic = obj.to_dictionary()
                list_dict.append(obj_dic)

        json_str = Base.to_json_string(list_dict)

        with open(file_name, 'w', encoding="utf-8") as fd:
            fd.write(json_str)


    @staticmethod
    def to_json_string(list_dictionaries):
        """ This is a method that return the JSON string reprsentation of
            list_dictionaries
        """

        if not list_dictionaries:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)
