#!/usr/bin/python3


class Square(Rectangle):
    """A class Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the Square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
