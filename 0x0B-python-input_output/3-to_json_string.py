#!/usr/bin/python3
"""
a function that returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Converts the given object to its JSON string representation.

    Args:
    - my_obj: The object to be converted.

    Returns:
    - A string containing the JSON representation of the given object.
    """
    return json.dumps(my_obj)
