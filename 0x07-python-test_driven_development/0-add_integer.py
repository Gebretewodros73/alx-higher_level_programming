#!/usr/bin/python3
"""Function that adds 2 integers.
    Args:
        a: int
        b: int, optional, default value is 98
"""
def add_integer(a, b=98):
    """The addition of a and b as an integer.
    Raises:
        TypeError: if a or b is not an integer."""

    if (not isinstance(a, int) and not isinstance (a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance (b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
