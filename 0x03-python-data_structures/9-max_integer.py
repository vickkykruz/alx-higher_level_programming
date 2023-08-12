#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    # CHECK IF THE LIST IS EMPTY
    if lenght == 0:
        return None
    # SORT THE LIST IN  AN ASCENDING ORDER
    my_list.sort()
    # GET THE HIGEST NUMBER
    highest_no = my_list.pop()
    return highest_no
