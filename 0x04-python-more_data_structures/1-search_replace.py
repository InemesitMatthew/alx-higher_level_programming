#!/usr/bin/python3


def search_replace(my_list, search, replace):
    # Create a new list to store the result
    new_list = []

    # Iterate through the elements in my_list
    for element in my_list:
        # Check if the element matches the search element
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    # Return the new list
    return new_list
