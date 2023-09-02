#!/usr/bin/python3
""" This is a function that divides all elements of a matrix

    Prototype: def matrix_divided(matrix, div)

    martix argument must be a list of integer or float otherwise raise a
    TypeError
    Each row of the matrix must be the same size otherwise raise a TypeError
    div must be a number otherwise raise a TypeError
    div can't be equal to 0 otherwise raise a ZeroDivisionError
    All element of the matrix should be divided by div
    Return a new martix
"""


def matrix_divided(matrix, div):
    """ Return a new matrix

    This function will validate the argument before returning the matrix """

    new_list = []

    for row in matrix:
        for data in row:

            if type(data) is not int and type(data) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "integers/floats")

    row_len = len(matrix[0])

    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [[round(num / div, 2) for num in row] for row in matrix]

    return new_list
