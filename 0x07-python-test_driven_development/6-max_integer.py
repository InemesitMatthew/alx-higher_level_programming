#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers

    Args:
    - list (list): The list of integers.

    Raises:
    - None

    Returns:
    - int: The maximum integer in the list.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


if __name__ == "__main__":
    print(max_integer([1, 2, 3, 4]))
    print(max_integer([1, 3, 4, 2]))
