#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Inherits from list."""

    def print_sorted(self):
        """Print a list in ascending order."""
        my_list = sorted(self)
        if my_list:
            print(my_list)
