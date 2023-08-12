#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lenght = len(my_list)
    # CHECK THE INDEX
    if idx < 0 or idx > lenght:
        return my_list

    # DELECT THE ITEX OF THE GIVEN INDEX
    del my_list[idx]
    return my_list
