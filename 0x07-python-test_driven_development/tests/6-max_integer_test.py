#!/usr/bin/python3
""" This ``6-max_integer`` is a unittest module

    Write a unittest for the function: def max_integer(list=[])
    Import the unittest module
    Run the command: ``python3 -m unittest tests.6-max_integer_test
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This class TestMaxInteger contains the test cases involued around the
    function def max_integer(list=[])
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertNotEqual(max_integer([10, 7, 9, 0, 12]), 10)
        self.assertEqual(max_integer(), None)

        matrix = [
                [1, 5, 7, 2],
                [1, 34, 17, 201],
                [0.1, 0.2, 0.25, 0.5],
                [0, 1, 17, -2],
                [-5, -200, 0, 0]
            ]

        for row in matrix:
            self.assertEqual(max_integer(row), max(row))
