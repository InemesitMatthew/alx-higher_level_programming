#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters added"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)


# Uncomment the following lines for testing
# nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
# print(nb_characters_added)
