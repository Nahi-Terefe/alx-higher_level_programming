#!/usr/bin/python3
""" A rectangle module """

from models.base import Base


class Rectangle(Base):
    """ A rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @property
    def height(self):
        """Getter"""
        return self.__height

    @property
    def x(self):
        """Getter"""
        return self.__x

    @property
    def y(self):
        """Getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """ width setter """
        self.__width = width

    @height.setter
    def height(self, height):
        """ height setter """
        self.__height = height

    @x.setter
    def x(self, x):
        """ x setter """
        self.__x = x

    @y.setter
    def y(self, y):
        """ y setter """
        self.__y = y
