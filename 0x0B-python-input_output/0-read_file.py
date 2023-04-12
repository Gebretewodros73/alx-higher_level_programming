#!usr/bin/python3
"""
Module documentation - read a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """

    print(open(filename, 'r', encoding='utf-8').read(), end="")
