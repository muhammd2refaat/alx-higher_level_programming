#!/usr/bin/python3
"""
Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and
age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves
a dictionary representation of a Student
instance (same as 8-class_to_json.py)
You are not allowed to import any module
"""


class Student:
    """Represents a student entity."""

    def __init__(self, given_name, family_name, years):
        """Creates a new Student instance with given
        name, family name, and years of age."""
        self.first_name = given_name
        self.last_name = family_name
        self.age = years

    def to_json(self):
        """Provides a dictionary with the student's attributes."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
