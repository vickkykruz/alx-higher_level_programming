#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    # COPY THE KEYS TO A NEW VARIABLE
    dicti = list(a_dictionary)
    if len(dicti) == 0:
        return None
    else:
        # GET THE FIRST VALUE OF THE DICTIONARY
        max_value = a_dictionary[dicti[0]]
        # GET THE FIRST KEY OF THE DICTIONARY
        name = dicti[0]
        # LOOP THROUGH EACH ELEMENT IN THE DICTIONARY
        for key, value in a_dictionary.items():
            # CHECK IF VALUE IS GREATER THAN THE INITAL MAX VALUE
            if value > max_value:
                max_value = value
                name = key
        return name
