#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class."""
    return type(obj) == a_class


# Test case
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print(f"{a} is an instance of the class {int.__name__}")
    if is_same_class(a, float):
        print(f"{a} is an instance of the class {float.__name__}")
    if is_same_class(a, object):
        print(f"{a} is an instance of the class {object.__name__}")
