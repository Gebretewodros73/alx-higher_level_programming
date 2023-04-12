#!usr/bin/python3
"""
Module documentation - read a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    print(open(filename, 'r', encoding='utf-8').read(), end="")
