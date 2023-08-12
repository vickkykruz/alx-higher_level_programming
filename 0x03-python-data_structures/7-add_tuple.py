#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    This functionis the add two tuple together, but before that is needed
    to get the length of each tuple, followed by a condition
    """
    lenA = len(tuple_a)
    lenB = len(tuple_b)

    # GIVE THE CONDITION
    if lenA >= 2:
        first_idx_A = tuple_a[0]
        second_idx_A = tuple_a[1]
    elif lenA == 1:
        first_idx_A = tuple_a[0]
        second_idx_A = 0
    elif lenA == 0:
        first_idx_A = 0
        second_idx_A = 0

    if lenB >= 2:
        first_idx_B = tuple_b[0]
        second_idx_B = tuple_b[1]
    elif lenB == 1:
        first_idx_B = tuple_b[0]
        second_idx_B = 0
    elif lenB == 0:
        first_idx_B = 0
        second_idx_B = 0

    tuple_add = (first_idx_A + first_idx_B, second_idx_A + second_idx_B)
    return tuple_add
