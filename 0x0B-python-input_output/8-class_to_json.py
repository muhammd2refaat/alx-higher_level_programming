#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:
Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable: list,
dictionary, string, integer and boolean
You are not allowed to import any module
"""


def class_to_json(obj):
    """
    Serializes an object's attributes into
    a dictionary that is suitable for
    JSON serialization, only including
    simpler data types
    """
    attribute_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            attribute_dict[key] = value
        elif isinstance(value, set):
            attribute_dict[key] = list(value)

    return attribute_dict
