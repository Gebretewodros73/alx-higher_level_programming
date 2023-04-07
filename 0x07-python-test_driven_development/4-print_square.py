def print_square(size):
    """
    # squares of n size.

    Args:
        size (int): length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
