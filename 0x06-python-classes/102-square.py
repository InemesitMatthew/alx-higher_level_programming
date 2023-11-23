class Square:
    """A class to represent a square and perform comparisons based on area."""

    def __init__(self, size=0):
        """
        Initialize the Square instance.

        Parameters:
        size (int or float): The size of the square.

        Raises:
        TypeError: If size is not a number.
        ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        value (int or float): The size to set.

        Raises:
        TypeError: If value is not a number.
        ValueError: If value is less than 0.
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        float: The area of the square.
        """
        return self.__size**2

    def __eq__(self, other):
        """
        Compare two squares for equality based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two squares for inequality based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare two squares for less than based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is less than, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two squares for less than or equal based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare two squares for greater than based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is greater than, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two squares for greater than or equal based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
