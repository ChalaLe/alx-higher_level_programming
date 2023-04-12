#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """ Class that inherits from list """
    def print_sorted(self):
        """ Prints sorted lists """
        print(sorted(self.copy()))
