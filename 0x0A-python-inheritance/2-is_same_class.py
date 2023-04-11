#!/usr/bin/python3
"""
Module documentation - identify the class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of the given a_class
    """

    return type(obj) == a_class
