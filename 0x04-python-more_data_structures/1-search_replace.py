#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # CHECK IF THE LIST IS NOT AN EMPTY LIST
    if len(my_list) == 0:
        return None
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
