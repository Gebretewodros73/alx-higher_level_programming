#!/bin/usr/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a: integer
    b: integer (default 98)

    Returns:
    The sum of a and b

    Raises:
    TypeError: if either a or b is not an integer

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
