#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file
"""


import sys

if __name__ == "__main__":
    try:
        filename = "add_item.json"
        try:
            my_list = load_from_json_file(filename)
        except FileNotFoundError:
            my_list = []
        my_list.extend(sys.argv[1:])
        save_to_json_file(my_list, filename)
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")
