#!/usr/bin/python3
"""
Module Documantation - which define square inherited from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ define square inheriting rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ square instance initialization """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Square representation """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ get size with getter method """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size with setter method """
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """ update key/value representation for square """
        if args is not None and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
