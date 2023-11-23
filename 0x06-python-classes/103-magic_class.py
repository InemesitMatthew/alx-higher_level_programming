import math


class MagicClass:
    """A class to perform operations equivalent to given Python bytecode."""

    def __init__(self, radius=0):
        """
        Initialize the MagicClass instance.

        Parameters:
        radius (int or float): The radius of the circle.

        Raises:
        TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    magic_circle = MagicClass(5)
    print("Area:", magic_circle.area())
    print("Circumference:", magic_circle.circumference())
