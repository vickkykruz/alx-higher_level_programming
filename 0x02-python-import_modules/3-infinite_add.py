#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as cmd_line
    i = 1
    add = 0
    lenght = len(cmd_line)
    while i < lenght:
        add += int(cmd_line[i])     # convert the input string to integer
        i += 1
    print("{}".format(add))
