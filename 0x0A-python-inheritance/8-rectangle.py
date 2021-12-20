#!/usr/bin/python3
""" Rectangel Class module """
from _typeshed import HasFileno


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangel(BaseGeometry):
    """ Rectangle Class """

    def __init__(self, width, height):
        """ Initalize an instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
