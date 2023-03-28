#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize a new square.
            size (int): the size of square
        """
        self._Square__size = size

    @property
    def size(self):
        """ set size of square"""
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """Return the current area of the square."""
        return self._Square__size ** 2
