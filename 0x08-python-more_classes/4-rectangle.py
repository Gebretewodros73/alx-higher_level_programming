#!/usr/bin/python3
"""
Module: Class  Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Class: class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = "#" * self.__width
        return "\n".join(rect_str for _ in range(self.__height))
