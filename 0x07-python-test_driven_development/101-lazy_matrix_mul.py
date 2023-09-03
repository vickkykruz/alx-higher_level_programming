#!usr/bin/python3
"""
    This a fuction that multiplies 2 matrices by using the module NumPy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        This is a function that multiples two times
    """

    mat_mul = np.matmul(m_a, m_b).tolist()

    return mat_mul
