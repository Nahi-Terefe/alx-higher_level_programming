#!/usr/bin/python3
""" A Geometry class """


class BaseGeometry():
    """ A BaseGeometry class """
    def area(self):
        """ Area of the geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate the passed value """
        if type(value) != int:
            raise TypeError(name + "must be an integer")
        elif value <= 0:
            raise ValueError(name + "must be greater than 0")
