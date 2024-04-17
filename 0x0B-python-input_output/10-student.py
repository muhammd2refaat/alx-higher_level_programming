#!/usr/bin/python3
"""
Write a class Student that defines a
student by: (based on 9-student.py)
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and
age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that
retrieves a dictionary representation of a
Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute
names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student with the given names and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """
        Converts the Student instance into a dictionary.
        When provided with a list of string attributes, only those
        specific attributes are included in the dictionary.
        If no list is provided, all attributes of the instance are included.
        """
        if (isinstance(attributes, list) and
                all(isinstance(attribute, str) for attribute in attributes)):
            return {
                attribute: getattr(self, attribute)
                for attribute in attributes if hasattr(self, attribute)
            }
        return self.__dict__
