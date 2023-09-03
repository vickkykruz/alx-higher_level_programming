#!/usr/bin/python3
""" Return a function that multiplies 2 matrices

    Prototype: def matrix_mul(m_a, m_b)

    m_a and m_b must be validate with these requirments in this order

    m_a and m_b must be an lists of integers or floats
        if m_a or m_b is not a list, raise TypeError with msg "m_a must be a"
        "list of lists" or "m_b must be a list of lists"

        if m_a or m_b is empty (means => [] or => [[]]) raise ValueError with
        msg "m_a can't be empty" or "m_b can't be empty"

        if one element of those lsit of lists is not an integer raise
        TypeError with msg "m_a should contain only integers or floats or
        "m_b should contain only integers or floats"

        if m_a or m_b is not a rectangl9all 'rows' should be the same) raise
        TypeError with msg "each row of m_a must be of the same size" or
        "each row of m_b must be of the same size"

        if m_a and m_b can't be multipled, raise ValueError with msg "m_a and
        m_b can't be multipled"
"""


def matrix_mul(m_a, m_b):
    """ Return the multiplied list of m_a and m_b """

    matrixes = [m_a, m_b]
    msg = ["m_a", "m_b"]

    for i in range(2):
        if type(matrixes[i]) is not list:
            raise TypeError("{} must be a list".format(msg[i]))

    for i in range(2):
        for row in matrixes[i]:
            if type(row) is not list:
                raise TypeError("{} must be a list of lists".format(msg[i]))

    for i in range(2):
        if len(matrixes[i]) == 0:
            raise ValueError("{} can't be empty".format(mgs[i]))

    for i in range(2):
        for row in matrixes[i]:
            for ele in row:
                if type(ele) is not int and type(ele) is not float:
                    raise TypeError("{} should contain only integers or floats"
                                    .format(msg[i]))

    for i in range(2):
        e_matrix = matrixes[i]
        matrix_lenght = len(e_matrix)
        for j in range(1, len(e_matrix)):
            if len(e_matrix[j]) != matrix_lenght:
                raise TypeError("each row of {} must be of the same size"
                                .format(msg[i]))

    col_size_m_a = len(m_a[0])
    row_size_m_b = len(m_b)
    if col_size_m_a != row_size_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for row in m_a:
        matr_row = []
        for j in range(len(m_b[0])):
            sum_mul = 0
            for i in range(col_size_m_a):
                sum_mul += row[i] * m_b[i][j]
            matr_row.append(sum_mul)
        new_matrix.append(matr_row)

    return new_matrix
