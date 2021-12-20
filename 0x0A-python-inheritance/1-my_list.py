#!/usr/bin/python3
""" MyList module """


class MyList(list):
    """ MyList clas """

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
