#!/usr/bin/python3
"""
Write a function that writes an Object to a
text file, using a JSON representation:
Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if
the object can’t be serialized.
You don’t need to manage file permission exceptions.
"""


def save_to_json_file(obj, file):
    """Serializes an object to a file in JSON format."""
    import json
    with open(file, 'w') as f:
        json.dump(obj, f)
