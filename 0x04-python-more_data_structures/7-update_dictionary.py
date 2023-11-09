#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    # If the key exists, replace the value
    # If the key doesn't exist, add a new key-value pair
    a_dictionary[key] = value
    # Return the updated dictionary
    return a_dictionary
