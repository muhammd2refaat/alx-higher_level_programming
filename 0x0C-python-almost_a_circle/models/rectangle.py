#!/usr/bin/python3
"""
The module contains the class rectangle
"""
from models.base import Base as theBaseClass


class Rectangle(theBaseClass):
    """
    Represents a geometric rectangle,
    extending the Base class functionality
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Construct a new Rectangle instance.

        Parameters:
            width (int): The horizontal size of the rectangle.
            height (int): The vertical size of the rectangle.
            x (int): The horizontal position of the rectangle's starting point.
            y (int): The vertical position of the rectangle's starting point.
            id (int): An identifier unique to this rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, dimension):
        """Update the width of the rectangle after validation."""
        # Check if the new width is acceptable.
        self.validation("width", dimension, False)
        self.__width = dimension

    @property
    def height(self):
        """Access the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, dimension):
        """Modify the height of the rectangle with proper validation."""
        # Validate and set the height value.
        self.validation("height", dimension, False)
        self.__height = dimension

    @property
    def x(self):
        """Access the x-coordinate (horizontal position) of the rectangle."""
        return self.__x

    @x.setter
    def x(self, coordinate):
        """Set the x-coordinate of the rectangle, with validation."""
        # Ensure the x-coordinate is valid.
        self.validation("x", coordinate)
        self.__x = coordinate

    @property
    def y(self):
        """Retrieve the y-coordinate (vertical position) of the rectangle."""
        return self.__y

    @y.setter
    def y(self, coordinate):
        """Assign a new y-coordinate to the rectangle after validation."""
        # Confirm the validity of the y-coordinate.
        self.validation("y", coordinate)
        self.__y = coordinate

    def validation(self, attribute, value, positive_only=True):
        """Validate the numerical value for a given property of the rectangle

        Ensures that the provided value conforms to the expected type and range

        Arguments:
            attribute (str): The name of the property being validated.
            value (int): The value to check against the validation rules.
            positive_only (bool): Determines if zero is an acceptable value.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))
        if positive_only and value < 0:
            raise ValueError("{} must be >= 0".format(attribute))
        elif not positive_only and value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """Compute the enclosed space of the rectangle."""
        # Multiplying the horizontal span with the vertical span to get area.
        horiz_span = self.width
        vert_span = self.height
        return horiz_span * vert_span

    def display(self):
        """Render the rectangle using the '#' symbol."""
        # Create the necessary vertical spacing before the rectangle.
        for vertical_space in range(self.y):
            print()
        # Print each row of the rectangle.
        for row in range(self.height):
            # Add horizontal spacing for the rectangle's position.
            print(" " * self.x, end="")
            # Display the row using the '#' symbol
            # for the width of the rectangle
            print("#" * self.width)

    def __str__(self):
        """Provide a human-readable representation of the rectangle."""
        return ("[Rectangle] ({id}) {x}/{y} - {width}/{height}"
                .format(id=self.id, x=self.x, y=self.y,
                        width=self.width, height=self.height))

    def update(self, *args, **kwargs):
        """update class atrbutes"""
        keys = ("id", "width", "height", "x", "y")
        for key, value in zip(keys, args):
            if key == "id" and not isinstance(value, int):
                continue
            setattr(self, key, value)
        if not args:
            for key, value in kwargs.items():
                if key == "id" and not isinstance(value, int):
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
