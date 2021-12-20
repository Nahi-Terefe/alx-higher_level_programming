#!/usr/bin/python3
""" A list module """


class Mylist(list):
    """ A list class """

    def print_sorted(self):
        """ Print a sorted list """
        print(sorted(self))
