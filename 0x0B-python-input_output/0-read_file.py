#!/usr/bin/python3
"""
Reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


# Uncomment the following lines for testing
# read_file("my_file_0.txt")
