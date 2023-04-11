#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: A Python object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
