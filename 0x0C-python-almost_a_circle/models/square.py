#!/usr/bin/python3
"""
The module contains the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square shape representation inheriting from Rectangle."""

    def __init__(self, dimension, x_axis=0, y_axis=0, identity=None):
        """Initialize a square with equal width and height.

        Parameters:
            dimension (int): The length of the sides of the square.
            x_axis (int): The horizontal offset of the square.
            y_axis (int): The vertical offset of the square.
            identity (int): Unique identifier for the square.
        """
        # Initialize the square as a special
        # case of rectangle with equal sides.
        super().__init__(dimension, dimension, x_axis, y_axis, identity)

    def __str__(self):
        """Provide a human-readable representation of the square."""
        return ("[Square] ({id}) {x}/{y} - {size}"
                .format(id=self.id, x=self.x, y=self.y, size=self.size))

    @property
    def size(self):
        """Size property to get or set the square's side length."""
        # The width attribute also represents the square's size.
        return self.width

    @size.setter
    def size(self, value):
        """Ensure both width and height are equal when setting the size."""
        # Setting size affects both width and height since it's a square.
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Modify the square's properties with updated values.

        This method can process both positional and keyword arguments to alter
        the square instance's current properties.

        When using *args:
            - First argument as 'None' re-initializes
            the instance with existing dimensions.
            - Subsequent arguments are assigned
            to properties in a set sequence.

        When using **kwargs:
            - Updates are made using named arguments.
            - Specifying 'id' as 'None' re-initializes the object's identity.

        Parameters:
            *args: A sequence of arguments that correspond to:
                - id (int): The unique ID, 'None' to reset.
                - size (int): Length of the square's sides.
                - x (int): The x-coordinate position.
                - y (int): The y-coordinate position.
            **kwargs: A dictionary of property names and values.

        Note:
            If both *args and **kwargs are provided, *args takes priority.
        """
        if args:
            # Property names in the expected order
            properties = ['id', 'size', 'x', 'y']
            for idx, prop in enumerate(properties):
                if idx < len(args):
                    # Assign argument based on index
                    setattr(self, prop, args[idx])
        else:
            for property_name, property_value in kwargs.items():
                # Update properties from keyword arguments
                setattr(self, property_name, property_value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
