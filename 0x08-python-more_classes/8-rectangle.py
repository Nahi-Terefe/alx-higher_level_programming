#!/usr/bin/python3
""" A rectangle class defination """


class Rectangle:
    """ A Rectangular class """

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method compare and return biggest rectangle instance """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangel")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangel")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        """ Initialize the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of this rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of this rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """ string representation of the rectangle """
        strOfRectangle = ""
        if self.__height == 0 or self.__width == 0:
            return strOfRectangle
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    strOfRectangle += "{}".format(self.print_symbol)
                strOfRectangle += "\n"
        return strOfRectangle[:-1]

    def __repr__(self):
        """ Representation of this instance as string """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Magic method to delete this rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
