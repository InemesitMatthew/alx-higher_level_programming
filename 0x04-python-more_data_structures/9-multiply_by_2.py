#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {keys: value * 2 for key, value in a_dictionary.items()}
    print(new_dict)

    return new_dict
