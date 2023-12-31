#!usr/bin/python3
"""
    This is a ``base_class`` module, we are tasked to do the following:
        => Create a class Base
            => Create a private class attribute __nb_objects = 0
            => Create a class construct: def __init__(self, id=None):
"""


import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ This is a method that save to file """
        filename = cls.__name__ + '.csv'
        new_list = []
        attrs = ["id", "size", "width", "height", "x", "y"]

        if list_objs:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                row = []

                for attr in attrs:
                    try:
                        row.append(obj_dict[attr])
                    except KeyError:
                        pass
                    new_list.append(row)

        with open(filename, 'w', encoding="utf-8") as fd:
            csv_write = csv.writer(fd, delimiter=",")

            if new_list:
                for row in new_list:
                    csv_write.writerow(row)
            else:
                csv_write.writerow(["[]"])

    @classmethod
    def load_from_file_csv(cls):
        """ This is a method that load file from csv """

        filename = cls.__name__ + '.csv'

        try:
            with open(filename, 'r', encoding="utf-8") as fd:
                if cls.__name__ == "Rectangle":
                    field_keys = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    field_keys = ["id", "size", "x", "y"]

                reader = csv.DictReader(fd, fieldnames=field_keys)
                new_list = []

                for row in reader:
                    for attr in field_keys:
                        row[attr] = int(row[attr])

                    new_ins = cls.create(**row)
                    new_list.append(new_ins)
        except FileNotFoundError:
            return []
        return new_list

    @classmethod
    def create(cls, **dictionary):
        """ This is a method that return an instance with all attributes
            already set
        """

        if cls.__name__ == "Rectangle":
            new_ins = cls(1, 1)

        if cls.__name__ == "Square":
            new_ins = cls(1)

        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        """ This is a method that returns a list of instance """

        new_list = []
        file_name = cls.__name__ + '.json'

        try:
            with open(file_name,  encoding="utf-8") as fd:
                json_str = fd.read()
        except FileNotFoundError:
            return new_list
        else:
            list_dic = Base.from_json_string(json_str)

        for obj in list_dic:
            new_ins = cls.create(**obj)
            new_list.append(new_ins)

        return new_list

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This is a method that return the JSON string reprsentation of
            list_dictionaries
        """

        if not list_dictionaries:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ This is a method that return the list of the JSON string
            reprsentation json_string
        """

        if not json_string:
            return json.loads([])
        else:
            return json.loads(json_string)
