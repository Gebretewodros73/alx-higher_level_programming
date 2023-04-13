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

        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """
        returns the valueeror and typeerror
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{name} must be greater than 0")
