#!/usr/bin/python3
"""Module for the Base class."""

import json
import csv
import turtle


class Base:
    """Base class for managing object IDs and providing serialization methods.

    Attributes:
        __nb_objects (int): Counter for tracking object IDs.

    Methods:
        __init__(self, id=None): Initializes a new instance of the Base class.
        to_json_string(list_dictionaries): Converts a list of dictionaries to a JSON string.
        from_json_string(json_string): Converts a JSON string to a list of dictionaries.
        save_to_file(list_objs): Saves a list of objects to a JSON file.
        load_from_file(): Loads objects from a JSON file.
        save_to_file_csv(list_objs): Saves a list of objects to a CSV file.
        load_from_file_csv(): Loads objects from a CSV file.
        draw(list_rectangles, list_squares): Draws rectangles and squares using Turtle graphics.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class.

        Args:
            id (int): The ID of the instance. If None, a new ID will be assigned.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON string representation of the list of dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to be converted.

        Returns:
            list: List of dictionaries.

        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to be saved.

        """
        filename = f"{cls.__name__}.json"
        json_list = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file.

        Returns:
            list: List of instances.

        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                return [cls.create(**obj) for obj in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to be saved.

        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fields = ["id", "size", "x", "y"]
            else:
                fields = []
            writer.writerow(fields)
            for obj in list_objs:
                writer.writerow([getattr(obj, field) for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file.

        Returns:
            list: List of instances.

        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                if cls.__name__ in ["Rectangle", "Square"]:
                    fields = reader.fieldnames
                    return [
                        cls.create(**{field: int(row[field]) for field in fields})
                        for row in reader
                    ]
                else:
                    return []
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        """
        screen = turtle.Screen()
        screen.bgcolor("white")

        # Draw rectangles
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)

        # Draw squares
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
