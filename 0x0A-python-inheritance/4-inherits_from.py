#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited from the specified class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class


# Test cases
if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
