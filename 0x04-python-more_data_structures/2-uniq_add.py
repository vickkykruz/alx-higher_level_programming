#!/usr/bin/python3
def uniq_add(my_list=[]):
    # CHECK IF THE LIST IS NOT AN EMPTY LIST
    if len(my_list) == 0:
        return None
    # REMOVE DUPLICATE ELEMENT IN THE LIST
    new_list = list(set(my_list))
    add = 0
    for ele in new_list:
        add += ele
    return add
