#!/usr/bin/python3
"""
Write a script that adds all arguments to
a Python list, and then save them to a file:
You must use your function save_to_json_file
from 5-save_to_json_file.py
You must use your function load_from_json_file
from 6-load_from_json_file.py
The list must be saved as a JSON representation
in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.
"""


from sys import argv
# Importing functions for JSON serialization and deserialization
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_file = "add_item.json"  # Renamed variable for clarity

# Attempt to load existing items from
# the JSON file, or initialize an empty list
try:
    list_of_items = load_from_json_file(json_file)
except FileNotFoundError:
    list_of_items = []

# Extend the list with the additional arguments provided by the user
list_of_items.extend(argv[1:])
# Write the updated list back to the JSON file
save_to_json_file(list_of_items, json_file)
