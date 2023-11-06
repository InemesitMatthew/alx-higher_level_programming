#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    element = my_list[idx]
    return element


# Example usage
if __name__ == "__main":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    result = element_at(my_list, idx)
    print("Element at index {:d} is {}".format(idx, result))
