#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Use list comprehension to create a new dictionary excluding keys with the specified value
    return {key: val for key, val in a_dictionary.items() if val != value}
