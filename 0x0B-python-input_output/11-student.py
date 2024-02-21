#!/usr/bin/python3
"""
Write a class Student that defines a
student by: (based on 10-student.py)
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with
        given first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """
        Convert the Student object to a dictionary.
        If attributes is a list of strings,
        only the specified attributes will be included.
        If attributes is none, all attributes will be included.
        """
        if isinstance(attributes,
                      list) and all(isinstance(attr,
                                               str) for attr in attributes):
            return {key: getattr(self,
                                 key) for key in attributes if hasattr(self,
                                                                       key)}
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

    def reload_from_json(self, update_data):
        """
        Update the Student instance's attributes
        with the values from the given dictionary.
        Only existing attributes will be updated.
        """
        for key, value in update_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
