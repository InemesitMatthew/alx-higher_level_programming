#!/usr/bin/python3
"""
Returns the dictionary description with a simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary description of obj for JSON serialization"""
    return obj.__dict__


# Uncomment the following lines for testing
# from 8-my_class import MyClass
# m = MyClass("John")
# m.number = 89
# print(type(m))
# print(m)
# mj = class_to_json(m)
# print(type(mj))
# print(mj)
