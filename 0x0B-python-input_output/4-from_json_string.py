#!/usr/bin/python3
"""
a function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string into a Python object.

    Args:
        my_str (str): A JSON string representing a Python object.

    Returns:
        obj: The Python object represented by the JSON string.

    Raises:
        ValueError: If the JSON string is invalid.

    """
    return json.loads(my_str)
