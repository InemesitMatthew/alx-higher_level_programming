#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num_printed = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            num_printed += 1
    except IndexError:
        pass  # Catch the IndexError (out of range) exception

    print()  # Add a new line after printing

    return num_printed


# Test the function with the provided examples
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
