#!usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    lenght = len(my_list)
    # CHECKING FOR THE CONDITION
    if idx < 0:
        return my_list
    elif idx >= lenght:
        return my_list
    else:
        # APPEND THE ITEMS IN THE ORIGINAL LIST TO THE NEW LIST
        for item in my_list:
            new_list.append(item)
        # MODIFED THE ELEMENT OF THE INDEX
        new_list[idx] = element
        return new_list
