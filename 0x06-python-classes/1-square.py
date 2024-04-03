#!/usr/bin/python3

"""This defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size):

        """ This creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
