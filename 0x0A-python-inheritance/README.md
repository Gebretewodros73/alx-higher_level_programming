# Python Inheritance Tasks

This directory contains a collection of tasks related to inheritance in Python. Each task explores different aspects of class inheritance, object-oriented programming, and method implementation.

## Table of Contents

1. [Lookup](#lookup)
2. [My List](#my-list)
3. [Exact Same Object](#exact-same-object)
4. [Same Class or Inherit From](#same-class-or-inherit-from)
5. [Only Subclass Of](#only-subclass-of)
6. [Geometry Module](#geometry-module)
7. [Integer Validator](#integer-validator)
8. [Rectangle](#rectangle)
9. [Full Rectangle](#full-rectangle)
10. [Square #1](#square-1)
11. [Square #2](#square-2)
12. [My Integer](#my-integer)
13. [Can I?](#can-i)

## Task Details

### 1. [Lookup](./0-lookup.py)

Write a function that returns the list of available attributes and methods of an object.

- Prototype: `def lookup(obj)`
- Returns: A list object
- No module imports allowed

### 2. [My List](./1-my_list.py)

Create a class `MyList` that inherits from `list`. Implement a public instance method `print_sorted()` that prints the list in ascending order.

### 3. [Exact Same Object](./2-is_same_class.py)

Write a function `is_same_class(obj, a_class)` that returns `True` if the object is exactly an instance of the specified class, otherwise `False`.

### 4. [Same Class or Inherit From](./3-is_kind_of_class.py)

Write a function `is_kind_of_class(obj, a_class)` that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

### 5. [Only Subclass Of](./4-inherits_from.py)

Write a function `inherits_from(obj, a_class)` that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

### 6. [Geometry Module](./5-base_geometry.py)

Create an empty class `BaseGeometry`.

### 7. [Integer Validator](./6-base_geometry.py)

Create a class `BaseGeometry` and add a public instance method `integer_validator(self, name, value)` to validate the value parameter.

### 8. [Rectangle](./7-base_geometry.py)

Create a class `Rectangle` that inherits from `BaseGeometry`. Implement instantiation with width and height, and ensure positive integers using the `integer_validator` method.

### 9. [Full Rectangle](./8-rectangle.py)

Create a class `Rectangle` that inherits from `BaseGeometry`. Implement the `area()` method and modify the `print()` and `str()` methods to display the rectangle description.

### 10. [Square #1](./9-rectangle.py)

Create a class `Square` that inherits from `Rectangle`. Implement instantiation with size and ensure positive integers using the `integer_validator` method.

### 11. [Square #2](./10-square.py)

Create a class `Square` that inherits from `Rectangle`. Modify the `print()` and `str()` methods to display the square description.

### 12. [My Integer](./100-my_int.py)

Create a class `MyInt` that inherits from `int` with inverted `==` and `!=` operators.

### 13. [Can I?](./101-add_attribute.py)

Write a function `add_attribute(obj, name, value)` that adds a new attribute to an object if possible.

Repository: [alx-higher_level_programming](https://github.com/gebretewodros73/alx-higher_level_programming)
Directory: 0x0A-python-inheritance

