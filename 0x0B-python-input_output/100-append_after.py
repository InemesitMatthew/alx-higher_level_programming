#!/usr/bin/python3
"""
Inserts a line of text to a file after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing search_string"""
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()


# Uncomment the following lines for testing
# if __name__ == "__main__":
#     append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
