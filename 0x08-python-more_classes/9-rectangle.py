#!/usr/bin/python3
"""
Module : Rectangle class to include a class method
square(cls, size=0) that returns a new Rectangle
instance with equal width and height, creating a square.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int): Keeps track of
        the number of Rectangle instances.
        print_symbol (any): The symbol used for
        string representation of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes
        a rectangle with optional width and height.
        area(self): Calculates and returns the area of
        the rectangle.
        perimeter(self): Calculates and returns the
        perimeter of the rectangle.
        __str__(self): Returns a string representation of
        the rectangle using print_symbol.
        __repr__(self): Returns a string representation of
        the rectangle to recreate a new instance.
        __del__(self): Prints a message when an instance
        of Rectangle is deleted.
        bigger_or_equal(rect_1, rect_2): Static method that
        returns the bigger rectangle based on area.
        square(cls, size=0): Class method that creates a
        new Rectangle instance as a square.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the
        rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol_rows = [str(self.print_symbol) * self.width for _ in range(self.height)]
        return "\n".join(symbol_rows)

    def __repr__(self):
        """Returns a string representation of the rectangle
        to recreate a new instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the bigger rectangle based on area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area.
            If both have the same area, rect_1 is returned.

        Raises:
            TypeError: If either rect_1 or rect_2 is
            not an instance of Rectangle.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method that creates a new Rectangle instance as a square.

        Args:
            size (int): The size of the square (equal width and height).

        Returns:
            Rectangle: A new Rectangle instance representing the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.

        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        return cls(size, size)
