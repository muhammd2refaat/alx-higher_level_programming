#!/usr/bin/python3
"""
Write a function that reads a text
file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Load a UTF-8 text file and display its contents to standard output."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
