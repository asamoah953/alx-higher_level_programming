#!/usr/bin/python3
"""
This module print_square
It prints a square with the character #.
"""


def print_square(cap):
    """Prints a square where size is
    the length and width of the square.
    """

    if type(cap) is not int:
        raise TypeError("cap must be an integer")

    if cap < 0:
        raise ValueError("size must be >= 0")

    for i in range(cap):
        for j in range(cap):
            print('#', end='')
        print()
