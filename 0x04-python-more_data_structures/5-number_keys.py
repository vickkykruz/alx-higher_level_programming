#!/usr/bin/python3
def number_keys(a_dictionary):
    counter = 0
    # LOOPING THROUGH THE DIC TO GET THE LENGTH
    for key, value in a_dictionary.items():
        counter += 1
    return counter
