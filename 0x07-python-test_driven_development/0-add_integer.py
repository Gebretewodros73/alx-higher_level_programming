#!/bin/usr/python3
""" define add_integer """


def add_integer(a, b=98):
    """Adds two integers.
    Raises: TypeError: if either a or b is not an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
