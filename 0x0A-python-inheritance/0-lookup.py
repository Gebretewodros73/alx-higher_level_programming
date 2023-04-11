#!/usr/bin/python3
"""define a method to lookup on objects"""


def lookup(obj):
    """
    The list of available attributes and methods

    Args:
        objec: The object to lookup.


    Return:
        A list of strings containing the available attributes and methods
    """
    #return sorted(vars(obj))return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or attr.startswith('__')]

    return [attr for attr in dir(obj)]
