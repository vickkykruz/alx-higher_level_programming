#!/usr/bin/python3
""" Return the <first name> <last name>

    Prototype: def say_my_name(first_name, last_name="")
    
    first_name and last_name must be strings otherwise, raise a TypeError with
    a message "first_name must be a string" or "last_name must be a string"
"""


def say_my_name(first_name, last_name=""):
    """ Return a msg "My name is <first_name> <last-name>

    Validate the arguments
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
