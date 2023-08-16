#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    num = 0
    divider = 0

    for ele in my_list:
        num += ele[0] * ele[1]
        divider += ele[1]

    return num / divider
