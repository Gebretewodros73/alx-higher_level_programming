#!/usr/bin/python3
"""
Module documentation - a function returns the number of characters
"""


def write_file(filename="", text=""):
    """
    manages to count number of characters text file (UTF8)
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
