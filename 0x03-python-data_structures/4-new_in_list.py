#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = [i for i in my_list]
    if idx < 0:
        return new_list
    if idx >= len(my_list):
        return new_list
    # CHANGE THE ELEMNET OF THE INDEX POSITION
    new_list[idx] = element
    return new_list
