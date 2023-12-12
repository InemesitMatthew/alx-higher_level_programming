#!/usr/bin/python3
"""Module for the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_positive_integer(self, attribute, value):
        """Validate that the value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def validate_non_negative_integer(self, attribute, value):
        """Validate that the value is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

    def area(self):
        """Compute and return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the Rectangle instance with '#' characters and handle x, y."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update attributes with arguments and key-worded arguments."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for index, arg in enumerate(args):
                setattr(self, attributes[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)  # Create a dummy instance
        elif cls.__name__ == "Square":
            new_instance = cls(1)  # Create a dummy instance
        else:
            return None

        new_instance.update(**dictionary)
        return new_instance

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
