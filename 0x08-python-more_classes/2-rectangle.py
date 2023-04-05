#!/usr/bin/python3

# 1-rectangle.py


""""A module that contains a rectangle class"""


class Rectangle:
    """a class Rectangle that defines a rectangle by
    instance width and height attribute"""

    def __init__(self, width, height):
        """It initialize the width and height of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width property setter that checks if if the type
        is integer or less than 0"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height property getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height property setter that checks if if the type
        is integer or less than 0"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
        self.__height = height

    def area(self):
        """Area() method that returns thge area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter() method that returns thge perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
