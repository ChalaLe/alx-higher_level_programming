#!/usr/bin/python3
"""
A function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
