#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list[:]

    if idx >= len(my_list):
        return my_list[:]

    copied_list = my_list[:]

    copied_list[idx] = element

    return copied_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)
