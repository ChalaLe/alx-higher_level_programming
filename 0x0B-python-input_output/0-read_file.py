#!/usr/bin/python3

"""
A function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
