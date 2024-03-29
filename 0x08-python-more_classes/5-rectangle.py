#!/usr/bin/python3
"""
Module : returns the rectangle area and perimeter
"""


class Rectangle:
    """A class representing a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """Return a string representation of the
        rectangle using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = "#" * self.__width
        return "\n".join(rect_str for _ in range(self.__height))

    def __del__(self):
        """Print a message when the rectangle instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
