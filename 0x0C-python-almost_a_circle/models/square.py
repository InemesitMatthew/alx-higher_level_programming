#!/usr/bin/python3
"""Module for the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes with arguments and key-worded arguments."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for index, arg in enumerate(args):
                setattr(self, attributes[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
