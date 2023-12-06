#!/usr/bin/python3
"""
Creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """Loads a JSON file and returns the corresponding object"""
    try:
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


# Uncomment the following lines for testing
# filename = "my_list.json"
# my_list = load_from_json_file(filename)
# print(my_list)
# print(type(my_list))
