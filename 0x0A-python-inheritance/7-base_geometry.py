#!/usr/bin/python3
"""
===================================
 	Class BaseGeometry in module
===================================
"""


class BaseGeometry:
    """The BaseGeometry class"""

    def area(self):
        """The method for calculating area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """The method for validating if a num is an integer or not"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
