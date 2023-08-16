#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	return list(x ** 2 for row in matrix for x in row )
