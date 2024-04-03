#!/usr/bin/python3

"""This section defines a class Square"""


class Square:
    """
    This is a class that defines properties of square by: (based on 4-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Arguments:
            size: the size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """This calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Arguments:
            value (int): size of a square (1 side).

        Raises:
            TypeError: the size must be an integer
            ValueError: the size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
