#!/usr/bin/python3
"""
    This is ``my_list`` modue that prit the list, but sorted

    def print_sorted(self):
"""


class MyList(list):
    """ This is a class MyList that is inherited from list """

    def print_sorted(self):
        """ This is a method that print the list, but sorted (ascending order)
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
