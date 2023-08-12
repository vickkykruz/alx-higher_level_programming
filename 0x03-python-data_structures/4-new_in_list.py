#!usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    lenght = len(new_list)
    # APPILY SOME CONDITIONS
    if idx < 0:
        return my_list
    elif idx >= lenght:
        return my_list
    # CHANGE THE ELEMENT IN THE POSITION
    new_list[idx] = element
    return new_list
