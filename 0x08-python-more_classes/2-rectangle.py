#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        if (type(height) != int):
            raise TypeError("height must be integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        if (type(width) != int):
            raise TypeError("width must be integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width


@property
def width(self):
    """Get/set the width of the Rectangle."""
    return self.__width


@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value


@property
def height(self):
    """Get/set the height of the Rectangle."""
    return self.__height


@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value


def area(self):
    """Return the area of the Rectangle."""
    return (self.__width * self.__height)


def perimeter(self):
    """Return the perimeter of the Rectangle."""
    if self.__width == 0 or self.__height == 0:
        return (0)
    return ((self.__width * 2) + (self.__height * 2))
