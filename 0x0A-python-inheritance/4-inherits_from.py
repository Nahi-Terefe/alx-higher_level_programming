#!/usr/bin/python3

""" inherits_from module """


def inherits_from(obj, a_class):
    """ Return True if the object is an instance that
    inherited from the specified """
    return isinstance(obj, a_class) and type(obj) != a_class
