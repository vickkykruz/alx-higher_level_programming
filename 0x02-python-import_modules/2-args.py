#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0   # initialize i to be zero
    lenght = len(argv)  # Get the total lenght of the argument passed
    if lenght == 2:
        print("{} argument:".format(lenght - 1))
    elif lenght == 1:
        print("{} arguments.".format(lenght - 1))
    else:
        print("{} arguments:".format(lenght - 1))

    for a in argv:
        if i == 0:
            i = i + 1
            continue
        print("{}: {}".format(i, a))
        i = i + 1
