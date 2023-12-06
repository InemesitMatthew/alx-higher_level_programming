#!/usr/bin/python3
"""
Writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj to a file using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)


# Uncomment the following lines for testing
# my_list = [1, 2, 3]
# save_to_json_file(my_list, "my_list.json")
# my_dict = {...}
# save_to_json_file(my_dict, "my_dict.json")
