#!usr/bin/python3
"""
Module documentation - read a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")
