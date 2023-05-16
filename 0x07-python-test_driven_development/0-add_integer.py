#!/usr/bin/python3
"""Function that adds 2 integers.
    Args:
        a: int
        b: int, optional, default value is 98
"""
def add_integer(a, b=98):
    """Function that adds 2 integers.
    Args:
        a: int
        b: int, optional, default value is 98
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: if a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
