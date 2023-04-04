#!/usr/bin/python3

"""Defining a locked class"""


class LockedClass:
    """It prevents the user from instantiating new
    LockedClass attributes"""

    __slots__ = ["first_name"]
