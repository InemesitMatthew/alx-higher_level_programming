#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                result_list.append(result)
            # Code to iterate through the lists and perform division
            except ZeroDivisionError:
                print("division by 0")
                # Code to handle division by zero
            except (TypeError, ValueError):
                print("wrong type")
                # Code to handle wrong types
    except IndexError:
        print("out of range")
        # Code to handle list length mismatch
    finally:
        return result_list
        # Code to handle common tasks (e.g., cleaning up)


# Test the function with the provided examples
if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
