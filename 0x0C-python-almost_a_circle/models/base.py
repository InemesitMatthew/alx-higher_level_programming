#!/usr/bin/python3
"""Module for the Base class."""


class Base:
    """The base class for managing the id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
