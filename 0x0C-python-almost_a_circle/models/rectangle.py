#!/usr/bin/python3
"""
Module Documentation : Rectangle class
"""
from models.base import Base


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

    def validate(self, name, value):
        """ validate all values """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if (name == "x" or name == "y") and value < 0:
            raise TypeError(f"{name} must be >= 0")

    @property
    def width(self):
        """ Get width attribute with getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width attribute with setter method """
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """ Get height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set width attribute """
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """ Get x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x attribute """
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """ Get y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set attribute """
        self.validate("y", value)
        self.__y = value

    def area(self):
        """define area module to return value of the Rectangle instance."""
        return self.__width * self.__height
