#!/usr/bin/python3
"""
Module documentation - identify if is in instance or in class
"""


def is_kind_of_class(obj, a_class):
    """
    Determines if an obect is an instance or a subclass of a given class

    Args:
        obj (any): The object to be checked.
        a_class (class): The class to check against.

    Returns:
        bool: True if the object is an instance or subclass of the class
    """

    return isinstance(obj, a_class)
