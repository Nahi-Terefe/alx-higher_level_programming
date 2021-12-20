#!/usr/bin/python3
""" A kind of class module """


def is_kind_of_class(obj, a_class):
    """ Checks if an obj is somehow an instance of
    this class or its parent class """
    return isinstance(obj, a_class)
