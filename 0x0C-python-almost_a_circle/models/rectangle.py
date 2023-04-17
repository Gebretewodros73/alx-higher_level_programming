#!/usr/bin/python3
from models.base import Base
"""
Module Documentation : Rectangle class
"""


class Rectangle(Base):
    """
    rectangle class with attribute width, height, x, and y of super id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get width attribute with getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width attribute with setter method """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Get height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set width attribute """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Get x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x attribute """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Get y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set attribute """

        if isinstance(value, int):
            raise TypeError("y must be and integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value
