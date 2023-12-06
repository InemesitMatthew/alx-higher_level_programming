#!/usr/bin/python3
"""
Returns an object (Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    return json.loads(my_str)


# Uncomment the following lines for testing
# s_my_list = "[1, 2, 3]"
# my_list = from_json_string(s_my_list)
# print(my_list)
# print(type(my_list))
# s_my_dict = "{'key': 'value'}"
# my_dict = from_json_string(s_my_dict)
# print(my_dict)
# print(type(my_dict))
