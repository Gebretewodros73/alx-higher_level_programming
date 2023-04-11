#!/usr/bin/python3
"""
Module documentation - returns true if only object is an instance of class
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is inherited from a class

    Args:
        obj (any): The object to be checked.
        a_class (class): The class to check against.

    Returns:
        bool: True if the object is an instance
    """

    return isinstance(obj, a_class) and type(obj) != a_class
