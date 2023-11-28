#!/usr/bin/python3
"""
Module to print "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print "My name is <first name> <last name>"

    Args:
    - first_name (str): The first name.
    - last_name (str, optional): The last name.

    Raises:
    - TypeError: If first_name or last_name is not a string.

    Returns:
    - None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
