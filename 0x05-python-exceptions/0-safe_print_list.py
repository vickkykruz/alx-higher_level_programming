#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0     # INITIZIATE A COUNTER FOR THE PROCESS

    for i in range(x):
        try:
            print(my_list[i], end="")
            counter += 1
        except IndexError:
            pass

    print()
    return counter
