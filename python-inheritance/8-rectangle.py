#!/usr/bin/python3
"""cretae an empty class claed BaseGeometry"""


class BaseGeometry:
    """define a calss caled BaseGeometry"""

    def area(self):
        """define area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            """the value must be  an int """
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            """the valu must be poitive int"""
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """a sub calss from basegemotry"""
