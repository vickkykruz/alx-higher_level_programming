#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = []

    for key, val in a_dictionary.items():
        if val == value:
            del_keys.append(key)
    for ele in del_keys:
        del a_dictionary[ele]

    return a_dictionary
