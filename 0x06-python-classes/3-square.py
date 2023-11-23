#!/usr/bin/python3
"""
3-square.py - Defines a Square class with an area method
"""


class Square:
    """
    The Square class represents a square.

    Attributes:
    - size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        -ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Parameters:
        - value (int): The size value.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size**2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
