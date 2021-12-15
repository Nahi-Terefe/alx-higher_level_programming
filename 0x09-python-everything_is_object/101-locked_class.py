#!/usr/bin/python3
"""
LockedClass
"""


class LockedClass:
    """ No class or object attributes, can't set
        Except for first_name
    """
    def __setattr__(self, atrr, value):
        if atrr == "first_name":
            self.__dict__[atrr] = value
        else:
            raise AttributeError("'LockedClass' \
                object has no atrr '" + atrr + "'")
