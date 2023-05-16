#!/bin/usr/python3
"""Function that adds 2 integers.
    Args:
        a: int
        b: int, optional, default value is 98
"""
def add_integer(a, b=98):
    """The addition of a and b as an integer.
    Raises:
        TypeError: if a or b is not an integer."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
