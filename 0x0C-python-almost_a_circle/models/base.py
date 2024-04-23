#!/usr/bin/python3
"""
The module contains the class Base
"""
import json
import csv


class Base:
    """ Base class """
    # private class attribute called __nb_objects
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the base class """
        # 1 - If id is not None, assign the public instance attribute id
        # with this argument value - you can assume id is an integer
        # and you don’t need to test the type of it
        if id is not None:
            self.id = id
        # Otherwise, increment __nb_objects and assign the new
        # value to the public instance attribute id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(dict_list):
        """Convert a list of dictionaries to a JSON string.

        Args:
            dict_list (list): A list of dictionaries to be
            converted to JSON string.

        Returns:
            str: The JSON string representation of dict_list.
            Returns an empty list
            as a JSON string if dict_list is None or empty.
        """
        if not dict_list:
            return "[]"
        return json.dumps(dict_list)

    @classmethod
    def save_to_file(cls, objects):
        """Save the JSON string representation of a list of objects to a file.

        The file is named after the class of the objects.

        Args:
            objects (list): A list of instances that inherit from Base.

        Side Effects:
            Writes the JSON string to a file with the name <ClassName>.json.
            If the list is None or empty, writes an empty list to the file.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as file:
            if objects is None:
                file.write("[]")
            else:
                object_dicts = [obj.to_dictionary() for obj in objects]
                file.write(Base.to_json_string(object_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representation of a list of
            dictionaries.

        Returns:
            list: A list of dictionaries represented by json_string.
            Returns an empty list if json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **attributes):
        """Instantiate an object from attribute dictionary.

        This method creates a new instance of the class upon which it's called
        (either Rectangle or Square) using a set of predefined initial values.
        The instance is then updated with the given attributes.

        Args:
            **attributes: Arbitrary keyword arguments containing attributes
            for the instance.

        Returns:
            The new, updated instance of the class.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        # Determine the class type and create a
        # new instance with default values.
        if cls is Rectangle:
            # Default width and height for Rectangle.
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)  # Default size for Square.
        else:
            instance = None  # In case cls is neither Rectangle nor Square.

        # Update instance with the provided attributes and return it.
        instance.update(**attributes)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file.

        This method loads objects from a JSON file and returns a list of
        instances of the class cls that were saved in the JSON file.

        Returns:
            list: A list of instances of the class cls that were
            saved in the JSON file.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                object_dicts = cls.from_json_string(file.read())
            instances = [cls.create(**obj) for obj in object_dicts]
            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Make a CVS class file represntation"""

        r_keys = ("id", "width", "height", "x", "y")
        s_keys = ("id", "size", "x", "y")
        class_name = cls.__name__
        list_dict = (
            [*map(lambda self: self.to_dictionary(), list_objs)]
            if list_objs else []
        )
        csv_list = []
        for inst_dict in list_dict:
            inst_list = []
            keys_list = inst_dict.keys()
            for key in s_keys if class_name == "Square" else r_keys:
                if key in keys_list:
                    inst_list.append(str(inst_dict[key]))
            if inst_list:
                csv_list.append(inst_list)

        with open(f"{class_name}.csv", "w") as f:
            if list_objs:
                if class_name == "Square":
                    f.write(",".join(s_keys) + "\n")
                elif class_name == "Rectangle":
                    f.write(",".join(r_keys) + "\n")
                for row in csv_list:
                    f.write(",".join(row) + "\n")
            else:
                f.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """Load a class from a CVS class file represntation"""
        class_name = cls.__name__
        try:
            with open(f"{class_name}.csv", "r") as f:
                inst_list = []
                for line in f:
                    if "id" in line:
                        continue
                    obj = cls(1) if class_name == "Square" else cls(1, 1)
                    obj.update(*map(int, line.split(",")))
                    inst_list.append(obj)
                return inst_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(rectangles, squares):
        """Draw both rectangles and squares using turtle graphics.

        This method takes a list of rectangle and square objects,
        creates a turtle for each one, sets a random pen color,
        and draws the shape on the screen.

        Args:
            rectangles: A list of rectangle objects to draw.
            squares: A list of square objects to draw.
        """
        import turtle
        import time
        from random import randrange

        # Set color mode for the turtle screen
        turtle.Screen().colormode(255)

        # Iterate over each shape in the combined
        # list of rectangles and squares
        for shape in rectangles + squares:
            # Create a new turtle instance for drawing
            artist = turtle.Turtle()
            # Set a random color for the turtle
            artist.color((randrange(255), randrange(255), randrange(255)))
            artist.pensize(1)  # Set the pen size to thin
            # Lift the pen to move it to a new starting position
            artist.penup()
            # Move turtle to start position
            artist.setpos((shape.x + artist.pos()[0],
                           shape.y - artist.pos()[1]))
            # Set the pen size thicker for drawing the shape
            artist.pensize(10)
            artist.pendown()   # Put the pen down to start drawing

            # Draw the shape based on its width and height
            artist.forward(shape.width)  # Draw the bottom edge
            artist.left(90)              # Turn left to draw the side
            artist.forward(shape.height)  # Draw the side edge
            artist.left(90)              # Turn left to draw the top
            artist.forward(shape.width)  # Draw the top edge
            artist.left(90)              # Turn left to draw the other side
            artist.forward(shape.height)  # Draw the other side edge
            artist.left(90)              # Turn left to complete the shape
            # Fill the shape (though it's not initialized)
            artist.end_fill()

        # Pause the screen for 5 seconds before closing
        time.sleep(5)
