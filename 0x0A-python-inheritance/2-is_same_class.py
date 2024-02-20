#!/usr/bin/python3
"""is same class"""


def is_same_class(obj, a_class):
    """Returns True if te object is exactly an instance of the specified class;
    otherwise False."""
    return type(obj) is a_class
