#!/usr/bin/python3
"""documentation"""


class MyList(list):
    """prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        """ method that prints a sorted list in ascending order"""
        print(sorted(self))
