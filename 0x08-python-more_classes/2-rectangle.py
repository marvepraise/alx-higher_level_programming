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
    return (self.__width)


@width.setter
def width(self, value):
    if (type(value) != int):
        raise TypeError("width must be integer")
    elif (value < 0):
        raise ValueError("width must be >= 0")
    else:
        self.__width = value


@property
def height(self):
    return (self.__height)


@height.setter
def height(self, value):
    if (type(value) != int):
        raise TypeError("height must be integer")
    elif (value < 0):
        raise ValueError("height must be >= 0")
    else:
        self.__height = value


def area(self):
    return (self.__width * self.__height)


def perimeter(self):
    if (self.__width <= 0 or self.__height <= 0):
        return 0
    else:
        return (2 * (self.__width + self.__height))
