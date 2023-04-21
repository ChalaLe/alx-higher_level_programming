#!/usr/bin/python3
"""Base class module"""

import json
import os
import csv
import turtle


class Base:
    """The `Base` class is the base of all other classes in the project"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Initializes a new instance of the `Base` class"""

        # Increment the number of objects and set the ID
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""

        # If the list is None, initialize it to an empty list
        if list_dictionaries is None:
            list_dictionaries = []
        # Check if the argument is a list of dictionaries
        elif type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")

        # Check if each item in the list is a dictionary
        for d in list_dictionaries:
            if type(d) is not dict:
                msg = "list_dictionaries must be a list of dictionaries"
                raise TypeError(msg)

        # Return the JSON string
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries"""

        # If the string is None, return an empty list
        if json_string is None:
            return []
        # Otherwise, parse the string and return the resulting list
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a file in JSON format"""

        # If the list is None, initialize it to an empty list
        if list_objs is None:
            list_objs = []

        # Construct the filename based on the class name
        filename = "{}.json".format(cls.__name__)

        # Write the JSON string to the file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects from a file in JSON format"""

        # Construct the filename based on the class name
        filename = "{}.json".format(cls.__name__)

        # If the file does not exist, return an empty list
        if not os.path.exists(filename):
            return []

        # Read the contents of the file and parse the JSON string
        ret = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())

            """ Create an object for each dictionary in
            the list and add it to the return list"""
            ret = [cls.create(**d) for d in list_dicts]

        # Return the list of objects
        return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of objects to a file in CSV format"""

        # If the list is None, initialize it to an empty list
        if list_objs is None:
            list_objs = []

        # Construct the filename based on the class name
        filename = "{}.csv".format(cls.__name__)

        # Define the attributes to be included in the CSV file
        attrs = ('id', 'size', 'width', 'height', 'x', 'y')

        with open(filename, "w", encoding="utf-8") as f:
            for o in list_objs:
                d = o.to_dictionary()
                t = []
                for attr in attrs:
                    if attr not in d:
                        continue
                    t.append(str(d.get(attr)))
                f.write(",".join(t))
                f.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """deserializes CSV"""
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                arguments = line[:-1].split(",")
                o = cls(1, 1)
                o.update(*[int(x) for x in arguments])
                list_objs.append(o)
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares
        """
        window = turtle.Screen()
        turtle.speed(5)
        turtle.pensize(5)
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.color("black")
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for colors in ["red", "yellow", "purple", "blue"]:
                turtle.color(colors)
                turtle.forward(square.size)
                turtle.left(90)
        turtle.penup()

        window.exitonclick()
