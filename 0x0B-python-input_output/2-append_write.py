#!/usr/bin/python3
"""
a function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The path to the file to append to
        If the file doesn't exist, it will be created.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    """
    with open(filename, 'a', encoding='utf=8') as f:
        """Append the text to the file and get the number
        of characters written"""
        return f.write(text)
