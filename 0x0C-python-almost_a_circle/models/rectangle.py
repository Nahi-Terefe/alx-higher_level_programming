#!/usr/bin/python3
""" A rectangle module """

from models.base import Base


class Rectangle(Base):
    """ A rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) != int:
            raise TypeError("y must be integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
