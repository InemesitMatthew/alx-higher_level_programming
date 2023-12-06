#!/usr/bin/python3
"""
Writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)


# Uncomment the following lines for testing
# nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# print(nb_characters)
