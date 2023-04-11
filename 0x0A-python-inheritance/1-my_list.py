#!/usr/bin/python3
"""Module documentation - MyList class"""


class MyList(list):
    """
    MyList class that inherits from list.

    Public instance method:
        - print_sorted(self): prints the list sorted in ascending order.

    Attributes:
        Inherits all attributes from the list class.
    """

    def print_sorted(self):
        """
        prints the list sorted in ascending order.
        """
        if not all(isinstance(i, int) for i in self):
            raise TypeError("List must be integers")
        print(sorted(self))
