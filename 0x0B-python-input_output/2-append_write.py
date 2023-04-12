#!/usr/bin/python3
"""
Module documentation - a function returns the number of append haracters
"""


def append_write(filename="", text=""):
    """
    manages to count number of append characters text file (UTF8)
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
