#!/usr/bin/python3
"""
Module documentation - identify if is in instance or in class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if it is an instance or class of the given
    """

    if isinstance(obj, a_class):
        return True
