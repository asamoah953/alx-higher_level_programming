#!/usr/bin/python3
"""A module for add_integer method"""


def add_integer(a, b=98):
    """Adds two integers.

    Arguments:
        a: first int.
        b: second int, default value is 98.

    Raises:
        TypeError: If a,and b are both not float.

    Returns:
        sum of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
