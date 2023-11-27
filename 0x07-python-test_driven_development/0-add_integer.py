#!/usr/bin/python3
"""
Module Name: 0-add_integer
Description: This module provides a function for adding two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :return: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
