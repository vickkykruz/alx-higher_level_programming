#!/usr/bin/python3
"""
    This is a ``pascal_triangle`` module contain a function
    def pascal_triangle(n): that return a list of lists of integer
    reprsentation
"""


def pascal_triangle(n):
    """ This is a function return a list of integers reprsenting pascal's
        triangle
    """

    new_list = []

    if n <= 0:
        return new_list

    new_list = [[1]]
    while len(new_list) != n:
        t_list = new_list[-1]
        tmp = [1]

        for i in range(len(t_list) - 1):
            tmp.append(t_list[i] + t_list[i + 1])
        tmp.append(1)
        new_list.append(tmp)
    return new_list
