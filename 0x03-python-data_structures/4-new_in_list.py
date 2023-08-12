#!usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list.copy(my_list)
    lenght = len(new_list)
    # CHECKING FOR THE CONDITION
    if idx < 0:
        return my_list
    elif idx >= lenght:
        return my_list
    else:
        # MODIFED THE ELEMENT OF THE INDEX
        new_list[idx] = element
        return new_list
