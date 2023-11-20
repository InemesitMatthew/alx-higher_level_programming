#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0

    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                num_printed += 1
    except IndexError as e:
        print("{}".format(e))

    print()  # Add a new line after printing integers
    return num_printed


# Test the function with the provided examples
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
