#!/usr/bin/python3


class Square:
    """
    Represent a square with size and position.

    Attributes:
    - size (int): The size of the square.
    - position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
        tuple: The position as a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Parameters:
        - value (tuple): The position as a tuple of 2 positive integers.

        Raises:
        TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print the square with the '#' character, considering the position.
        """
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: String representation of the square.
        """
        result = []
        for _ in range(self.position[1]):
            result.append("")
        for _ in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)
        return "\n".join(result)


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    # Output:
    # #####
    # #####
    # #####
    # #####
    # #####

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)

    # Output:
    #     #####
    #     #####
    #     #####
    #     #####
    #     #####
