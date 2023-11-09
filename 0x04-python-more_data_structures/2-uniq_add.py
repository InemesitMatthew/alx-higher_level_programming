#!/usr/bin/python3


def uniq_add(my_list=None):
    if my_list is None:
        my_list = []
    # Create an empty set to store unique integers
    unique_set = set()
    # Initialize a variable to store the sum
    sum_unique = 0

    # Iterate through the elements in my_list
    for element in my_list:
        # Check if the element is not in the set
        if element not in unique_set:
            # Add the element to the set
            unique_set.add(element)
            # Add the element to the sum
            sum_unique += element

    # Return the sum of unique integers
    return sum_unique
