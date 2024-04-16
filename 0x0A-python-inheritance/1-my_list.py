#!/usr/bin/python3
"""
===========================
This module is with the class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """This method sorts a list"""

        print(sorted(list(self)))
