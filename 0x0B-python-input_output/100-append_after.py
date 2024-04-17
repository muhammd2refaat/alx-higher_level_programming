#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):
Prototype: def append_after(filename="",
search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission
or file doesn't exist exceptions.
You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Adds a new line of text immediately following
    any line that contains a specified string.
    """
    with open(filename, 'r') as f:
        content_lines = f.readlines()

    with open(filename, 'w') as f:
        for content in content_lines:
            f.write(content)
            if search_string in content:
                f.write(new_string)
