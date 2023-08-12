#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lenght = len(my_list)
    new_list = my_list
    # CHECK THE INDEX
    if idx < 0 or idx >= lenght:
        return new_list

    # DELECT THE ITEX OF THE GIVEN INDEX
    del new_list[idx]
    return new_list
