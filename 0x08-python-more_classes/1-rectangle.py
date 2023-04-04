#!/usr/bin/python3
"""
Module: 1-rectangle
Defines a Rectangle Class.
"""


class Rectangle:
    """
    Defines a Rectangle Object.
    """
    def __init__(self, width=0, height=0):
        """
        initializes a new Rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns: the current width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width
        value(int): new width
        Raises:
            TypeError: if value not integer
            ValueError: if value is less than 0.
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Returns: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
            value(int): new height.
        Raises:
            TypeError: if value not integer
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
