#!/usr/bin/python3


class BaseGeometry:
    """A class with an empty implementation of area method."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")


# Test cases
if __name__ == "__main__":
    bg = BaseGeometry()
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
