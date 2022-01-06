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
        """ Width Getter - Read Value """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter width - change value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height Getter - Read Value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter height - change value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x Getter - Read Value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter x - change value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y Getter - Read Value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter y - change value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ returns area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ displays the this rectangle instance """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """ Str format """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)
