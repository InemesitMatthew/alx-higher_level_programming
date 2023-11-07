#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Handle tuple size by unpacking with default values
    a_1, a_2 = tuple_a if len(tuple_a) >= 2 else (0, 0)
    b_1, b_2 = tuple_b if len(tuple_b) >= 2 else (0, 0)

    # Perform addition
    result_1 = a_1 + b_1
    result_2 = a_2 + b_2

    # Return the resulting tuple
    return (result_1, result_2)


# Example usage
if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
