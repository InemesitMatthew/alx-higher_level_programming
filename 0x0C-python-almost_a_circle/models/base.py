#!/usr/bin/python3
"""Module for the Base class."""

import json


class Base:
    """Base class for other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a file in JSON format."""
        if list_objs is None:
            list_objs = []
        json_data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as file:
            file.write(json_data)
