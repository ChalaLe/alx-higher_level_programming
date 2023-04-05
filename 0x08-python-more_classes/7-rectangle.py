#!/usr/bin/python3

# 1-rectangle.py


""""A module that contains a rectangle class"""


class Rectangle:
    """a class Rectangle that defines a rectangle by
    instance width and height attribute"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """It initialize the width and height of rectangle"""
        type(self).number_of_instances += 1
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

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recta_array = []
        for i in range(self.__height):
            [recta_array.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                recta_array.append("\n")
        return ("".join(recta_array))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
