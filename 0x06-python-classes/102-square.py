#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Represenr square class"""

    def __init__(self, size=0):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define == comparison to square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define != comparison to square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define < comparison to square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define <= comparison square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define > comparison to square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define >= comparison to square"""
        return self.area() >= other.area()
