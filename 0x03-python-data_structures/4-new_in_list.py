#!usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    lenght = len(new_list)
    # APPILY SOME CONDITIONS
    if idx < 0 or idx >= lenght:
        return my_list
    new_list[idx] = element
    return new_list
