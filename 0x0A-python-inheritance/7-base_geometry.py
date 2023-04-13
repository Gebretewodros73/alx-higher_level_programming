#!/usr/bin/python3
"""
Module documentation - defines empty class
"""


class BaseGeometry():
    """
    BaseGeometry defined with module of area
    """

    def area(self):
        """
        define area with out any implementation
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates and integer value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
