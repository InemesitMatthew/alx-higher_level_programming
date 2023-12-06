#!/usr/bin/python3
"""
Returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj"""
    return json.dumps(my_obj)


# Uncomment the following lines for testing
# my_list = [1, 2, 3]
# s_my_list = to_json_string(my_list)
# print(s_my_list)
# print(type(s_my_list))
# my_dict = {...}
# s_my_dict = to_json_string(my_dict)
# print(s_my_dict)
# print(type(s_my_dict))
